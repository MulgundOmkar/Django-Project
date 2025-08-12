from django import forms
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from .models import CustomUser
import re

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['name', 'email', 'phone', 'password']

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 8:
            raise forms.ValidationError('Must be 8 characters long')
        if not re.search(r'[A-Z]', password):
            raise forms.ValidationError('Must contain a capital letter')
        if not re.search(r'[\W_]', password):
            raise forms.ValidationError('Must contain a special character')
        return password

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
