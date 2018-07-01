from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='使用者')
    phone = models.CharField('手機', max_length=12, validators=[
        RegexValidator(
            regex='^09\d{2}-?\d{3}-?\d{3}$',
            message='手機格式不符合',
        )
    ])
    address = models.CharField('地址', max_length=150)

    def __str__(self):
        return str(self.phone)

    class Meta:
        verbose_name = '使用者'
        verbose_name_plural = '使用者'