from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.template.loader import get_template
from django.template import loader

from django.contrib import messages as m
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import UserForm, ProfileForm
# from django.contrib.auth.models import User  引入 Django 套件抓使用者資料
# from django.contrib.auth import get_user_model  如果自己有改 Ｍodel 可以使用這個來抓使用者資訊

from .forms import UserModelForm
from django.contrib.auth.decorators import login_required
from .models import Profile


def register(request):
    # form = UserCreationForm(request.POST or None)
    form = UserForm(request.POST or None)
    profile_form = ProfileForm(request.POST or None)

    if form.is_valid() and profile_form.is_valid():
        user = form.save()
        profile = profile_form.save(commit=False)
        profile.user = user
        profile.save()
        # print(user.email) Check user email is saved
        login(request, user)
        return redirect(reverse('books:index'))

    return render(request, 'registration/form.html', {'form': form, 'profile_form': profile_form})

@login_required
def edit(request):
    # user = get_object_or_404(get_user_model(), pk=request.user.pk)
    # 在這裡沒有使用套件的原因是會修改使用者資訊一定是已經登入的狀況下, 所以只需要確認是否是登入的狀態下就行
    form = UserModelForm(request.POST or None, instance=request.user)

    if Profile.objects.filter(user=request.user).exists():
        profile = request.user.profile
    else:
        profile = Profile()

    profile_form = ProfileForm(request.POST or None, instance=profile)

    if form.is_valid() and profile_form.is_valid():
        form.save()
        profile_form.save()
        return redirect('books:index')

    return render(request, 'registration/edit_form.html', {'form':form, 'profile_form': profile_form})