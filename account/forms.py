from django import forms
from django.contrib.auth.models import User
from account.models import UserProfile


class LoginForm(forms.Form):
    username = forms.CharField(max_length=32)
    password = forms.CharField(widget=forms.PasswordInput)


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label="密&nbsp;&nbsp;&nbsp;码:", widget=forms.PasswordInput)
    password2 = forms.CharField(label="确认密码:", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('输入的密码不一致!')
        return cd['password2']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone', 'birth')
