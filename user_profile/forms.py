from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from user_profile.models import *
class LoginForm(AuthenticationForm,forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password',)
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password','email')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


# class UserForm(forms.ModelForm):
#     model =