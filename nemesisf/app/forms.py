from django import forms
from .models import Login,Signup



class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = ['email','password']
        widgets = {'password':forms.PasswordInput}


class SignupForm(forms.ModelForm):
    class Meta:
        model = Signup
        fields = ['username','email','password','confirm_password','address']
        widgets = {'password':forms.PasswordInput, 'confirm_password':forms.PasswordInput}