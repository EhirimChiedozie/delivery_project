from django.contrib.auth.forms import UserCreationForm
from .models import Customer
from django import forms
from django.contrib import messages

class AccountOpeningForm(UserCreationForm):
    class Meta:
        model = Customer
        fields = ['email', 'password1', 'password2']