from django.forms import ModelForm, Form, BooleanField, EmailField, CharField
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from .models import Profile
User = get_user_model()

class UserModelForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')


class UserForm(UserCreationForm): # class <ClassName>(parent):
    email = EmailField(
        label="電子信箱",
    )
    first_name = CharField(label="名字",)
    last_name = CharField(label="姓氏",)

    def clean_email(self):
        '''
        Now you can know...
        The clean_<field_name> will be call before is_valid
        Your return data is final data to be save to the model's <field_name>
        '''
        email = self.cleaned_data.get("email") # Get data from `form` (means data maybe not in database)
        # test email is exists?
        user = User.objects.filter(email=email) # Get data from `model` (data has be saved in database)
        if user:
            raise ValidationError('此信箱已使用過')
        return email
        
    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name")
        field_classes = {'username': UsernameField}


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('phone', 'address')