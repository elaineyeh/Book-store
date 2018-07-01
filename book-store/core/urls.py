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
from django.urls import path, include
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views

from accounts.views import register, edit

from django.conf import settings
from django.conf.urls.static import static


# def root(x):
#     return redirect('books:index')


urlpatterns = [
    path('', lambda x: redirect('books:index'), name='root'),
    path('admin/', admin.site.urls),
    path('books/', include('books.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('edit/', edit, name='edit'),
    path('accounts/', include('accounts.urls')),
    path('orders/', include('orders.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
