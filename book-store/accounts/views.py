from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.template.loader import get_template
from django.template import loader

from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
# from django.contrib.auth.models import User  引入 Django 套件抓使用者資料
# from django.contrib.auth import get_user_model  如果自己有改 Ｍodel 可以使用這個來抓使用者資訊

from .forms import UserModelForm


def register(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect(reverse('registration'))

    return render(request, 'registration/form.html', {'form':form})

def edit(request):
    # user = get_object_or_404(get_user_model(), pk=request.user.pk)
    # 在這裡沒有使用套件的原因是會修改使用者資訊一定是已經登入的狀況下, 所以只需要確認是否是登入的狀態下就行
    if request.user.is_authenticated:
        form = UserModelForm(request.POST or None, instance=request.user)

        if form.is_valid():
            user = form.save()
            return redirect(reverse('books:index'))
    return render(request, 'registration/edit_form.html', {'form':form})

def registration(request):
    if request.user.is_authenticated:
        form = UserModelForm(request.POST or None, instance=request.user)

        if form.is_valid():
            user = form.save()
            return redirect(reverse('books:index'))
    return render(request, 'registration/registration_form.html', {'form':form})