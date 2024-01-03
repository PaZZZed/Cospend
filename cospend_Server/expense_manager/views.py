from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import ExpenseForm, GroupForm, EditGroupForm
from .models import Expense, Group, Balance
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseForbidden



# home views to redirect either to login or register
def home(request):
    return render(request, "expense_manager/home.html")


# Registration View
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")  # Redirect to a home page or other appropriate page
    else:
        form = UserCreationForm()
    return render(request, "expense_manager/register.html", {"form": form})


@login_required
def info(request):
    return render(request, "expense_manager/info.html")


def manage_groupe(request):
    # print(dir(request))
    owned_groups = Group.objects.filter(
        owner=request.user
    )  # Fetch groups owned by the user

    if request.method == "POST":
        form = GroupForm(request.POST or None, user=request.user)
        if form.is_valid():
            group_name = form.cleaned_data["name"]
            group = Group.objects.create(owner=request.user, name=group_name)
            group.members.set(form.cleaned_data["members"])
            group.members.add(request.user)
            for member in group.members.all():
                Balance.objects.create(user=member, group=group, amount=0)

            # Redirect to the desired page, e.g., back to the info or group list page
            return redirect("manage_groupe")
    else:
        form = GroupForm(user=request.user)

    # Pass both form and owned_groups to the template
    return render(
        request,
        "expense_manager/manage_groupe.html",
        {"form": form, "owned_groups": owned_groups},
    )


@login_required
def edit_group(request, id):
    group = get_object_or_404(Group, id=id, owner=request.user)

    if request.method == "POST":
        form = EditGroupForm(request.POST, group=group)

        # Check if no members are selected
        if "members" not in request.POST:
            group.delete()
            return redirect("manage_groupe")

        if form.is_valid():
            selected_members = form.cleaned_data.get("members")
            group.members.set(selected_members)
            group.members.add(group.owner)  # Ensure the owner remains a member
            return redirect("manage_groupe")

    else:
        form = EditGroupForm(group=group)

    return render(
        request, "expense_manager/edit_group.html", {"form": form, "group": group}
    )


@login_required
def manage_expense(request):
    groups = Group.objects.filter(members=request.user)
    return render(request, "expense_manager/manage_expense.html", {"groups": groups})


@login_required
def create_expense(request, group_id):
    group = get_object_or_404(Group, id=group_id)

    if request.user not in group.members.all():
        return HttpResponseForbidden()
    
    balances = Balance.objects.filter(group=group)

    if request.method == 'POST':
        form = ExpenseForm(request.POST, user=request.user, group=group)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.paid_by = request.user
            expense.group = group
            expense.save()
            form.save_m2m()  # Save the many-to-many data

            involved_members = expense.involved_members.all()
            if involved_members.exists():  # Check if there are involved members
                total_amount = expense.amount
                share_amount = total_amount / len(involved_members)

                # Update the balance for each involved member
                for member in involved_members:
                    balance, _ = Balance.objects.get_or_create(user=member, group=group)
                    if member == request.user:
                        balance.amount += total_amount - share_amount
                    else:
                        balance.amount -= share_amount
                    balance.save()

            return redirect('manage_expense')

    else:
        form = ExpenseForm(user=request.user, group=group)

    return render(request, 'expense_manager/create_expense.html', {'form': form, 'balances': balances})


@login_required
def consult_expenses(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    if request.user not in group.members.all():
        return HttpResponseForbidden()

    expenses = Expense.objects.filter(group=group)
    return render(request, 'expense_manager/consult_expenses.html', {'group': group, 'expenses': expenses})
