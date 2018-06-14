"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, reverse_lazy

from django.contrib.auth.views import PasswordChangeView, PasswordResetView, PasswordResetConfirmView

from . import views


login_parms = dict(
    redirect_authenticated_user=True,
    template_name='users/login.html',
)

password_change_parms = dict(
    template_name='users/password_change.html',
    success_url=reverse_lazy('login'),
)

password_reset_parms = dict(
    template_name='users/password_reset.html',
    subject_template_name='users/password_reset_subject.txt',
    email_template_name='users/password_reset_email.html',
    html_email_template_name='users/password_reset_html_email.html',
    success_url=reverse_lazy('login')
)

password_reset_confirm_parms = dict(
    template_name='users/password_reset_confirm.html',
    post_reset_login=True,
    success_url=reverse_lazy('login')
)

# dict() == {form:form}


app_name = 'accounts'
urlpatterns = [
    path('password-change/', PasswordChangeView.as_view(**password_change_parms), 
        name='password_change'),
    path('password-reset/', PasswordResetView.as_view(**password_reset_parms), 
        name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(**password_reset_confirm_parms),
        name='password_reset_confirm'),
]
