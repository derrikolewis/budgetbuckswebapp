from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register', views.registerPage, name='register'),
    path('password/', views.PasswordsChangeView.as_view(template_name='budget/change-password.html')),
    path('password_success', views.password_success, name="password_success"),
    path('edit-profile', views.UserEditView.as_view(), name='edit-profile'),
    path('about', views.aboutus, name='about'),
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('', views.home, name='home'),
    path('list', views.project_list, name='list'),
    path('add', views.ProjectCreateView.as_view(), name='add'),
    path('<slug:project_slug>', views.project_detail, name='detail'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='budget/password_reset.html'), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='budget/password_reset_sent.html'), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='budget/password_reset_form.html'), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='budget/password_reset_done.html'), name="password_reset_complete"),
]