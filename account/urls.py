from django.urls import path
from django.contrib.auth import views as auth_views
from account import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='user_login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='account/logout.html'), name='user_logout'),
    path('register/', views.register, name='user_register'),

    path('password_change/', auth_views.PasswordChangeView.as_view(
        template_name='account/password_change_form.html', success_url="/account/password_change_done/"),
         name='password_change'),

    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='account/password_change_done.html'), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name="account/password_reset_form.html",
        email_template_name="account/password_reset_email.html",
        success_url='/account/password_reset_done/'),
         name='password_reset'),

    path('password_reset_done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='account/password_reset_done.html'), name='password_reset_done'),

    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name="account/password_reset_confirm.html",
        success_url='/account/password_rest_complete/'),
         name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='account/password_reset_complete.html'), name='password_reset_complete'),
    path('myself/', views.myself, name="myself"),
    path('myself_edit/', views.myself_edit, name="myself_edit")
]
