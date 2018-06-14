from django.forms import ModelForm, Form, BooleanField
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
User = get_user_model()

class UserModelForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('email',)

    def clean_email(self):
        # Get the email
        email = self.cleaned_data.get('email')

        # Check to see if any users already exist with this email as a username.
        try:
            match = User.objects.get(email=email)
        except User.DoesNotExist:
            # Unable to find a user, this is fine
            return email

        # A user was found with this as a username, raise an error.
        raise forms.ValidationError('This email address is already in use.')