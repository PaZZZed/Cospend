# forms.py
from django import forms
from django.contrib.auth.models import User

from .models import Expense


class GroupForm(forms.Form):
    name = forms.CharField(label="Group Name", max_length=100)
    members = forms.ModelMultipleChoiceField(
        queryset=User.objects.none(), widget=forms.CheckboxSelectMultiple
    )

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super(GroupForm, self).__init__(*args, **kwargs)
        if user:
            self.fields["members"].queryset = User.objects.exclude(id=user.id)


class EditGroupForm(forms.Form):
    members = forms.ModelMultipleChoiceField(
        queryset=User.objects.none(), widget=forms.CheckboxSelectMultiple
    )

    def __init__(self, *args, **kwargs):
        group = kwargs.pop("group", None)
        super(EditGroupForm, self).__init__(*args, **kwargs)
        if group:
            self.fields["members"].queryset = User.objects.exclude(id=group.owner.id)
            self.fields["members"].initial = group.members.exclude(id=group.owner.id)


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['title', 'amount', 'date', 'description', 'involved_members']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        group = kwargs.pop("group", None)
        super(ExpenseForm, self).__init__(*args, **kwargs)
        self.fields['involved_members'].disabled = True
        self.fields['involved_members'].required = False
        if group:
            self.fields["involved_members"].queryset = group.members.all()
