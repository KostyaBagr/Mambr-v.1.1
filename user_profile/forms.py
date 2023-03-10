from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from user_profile.models import *

class LoginForm(AuthenticationForm,forms.ModelForm):
    class Meta:
        model = MyUserProfile
        fields = ('username',)
    # username = forms.CharField()
    # password1 = forms.CharField(widget=forms.PasswordInput)
    # password2 = forms.CharField(widget=forms.PasswordInput)


class CreateUserProfile(UserCreationForm):
    class Meta:
        model = MyUserProfile
        # fields ='__all__'
        fields =('username','email')
        labels= {'username':'Ваше имя'}


        # widgets = {
        #     'password1': forms.TextInput(attrs={'': 'form-control'}),
        #
        # }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.set_password(self.cleaned_data["password2"])
        if commit:
            user.save()
        return user

class CustomUserProfile(UserChangeForm):
    class Meta:
        model = MyUserProfile
        fields =('username', 'email', 'bio', 'photo')
        exclude = ['password']
