from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import api_views
from . import views

urlpatterns = [
    path('manage_groupe/api/public_key/', views.get_public_key, name='get_public_key'),
    path('api/get-user-public-keys/', api_views.get_user_public_keys, name='get_user_public_keys'),


    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    # path('login/', views.login, name='login'),
    path("login/",LoginView.as_view(template_name="registration/login.html", success_url="/info/"), name="login",),
    path("info/", views.info, name="info"),
    path("manage_groupe/", views.manage_groupe, name="manage_groupe"),
    path("logout/", LogoutView.as_view(next_page="/cospend/"), name="logout"), 
    path('edit_group/<int:id>/', views.edit_group, name='edit_group'),
    path('create_expense/<int:group_id>/', views.create_expense, name='create_expense'),
    path('manage_expense/', views.manage_expense, name='manage_expense'),
    path('consult_expenses/<int:group_id>/', views.consult_expenses, name='consult_expenses'),

]
