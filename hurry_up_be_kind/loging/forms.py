from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, PasswordInput, IntegerField, CharField
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField



class SignupForm(UserCreationForm):
    phone = CharField(max_length=12, help_text="Статус")
    status = CharField(max_length=100, help_text="Статус")

    class Meta:
        model = User
        fields = ('password1', 'password2', )