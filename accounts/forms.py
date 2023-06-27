from django import forms
from .models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='password reply', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username',)

    def clean_password(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 !=password2:
            raise ValueError('you have to enter password')
        return password2
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) < 4 :
            raise ValueError('username must have at least 4 char')
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')

        if email:
            raise ValidationError('Email is exist please enter another one')
        return email
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password1'))
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('username','email','password','mobile','is_active','is_admin')
        
    
