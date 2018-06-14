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
from django.urls import path

from . import views as v


app_name = 'orders'
urlpatterns = [
    path('', v.index, name='index'), #所有訂單
    path('<int:pk>/', v.show, name='show'), #某訂單明細
    path('paid/', v.paid, name='paid'), #確認結帳
    path('shopcars/', v.shopcar_index, name='shopcars'), #購物車
    path('shopcars/<int:pk>/delete/',
         v.shopcar_delete,
         name='shopcars_delete'), #刪除某項訂單
]
