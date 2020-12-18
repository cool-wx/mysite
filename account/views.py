from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from account.forms import LoginForm, RegistrationForm, UserProfileForm


# Create your views here.
def user_login(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user:
                login(request, user)
                return HttpResponse('success!')
            else:
                return HttpResponse('false')

    if request.method == "GET":
        login_form = LoginForm()
        return render(request, "account/login.html", {"form": login_form})


def register(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        userprofile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and userprofile_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            new_profile = userprofile_form.save(commit=False)
            new_profile.user = new_user
            new_profile.save()
            return HttpResponse('ok')
        else:
            return HttpResponse('false')
    else:
        user_form = RegistrationForm()
        userprofile_form = UserProfileForm()
        return render(request, 'account/register.html', {"user_form": user_form, "userprofile_form": userprofile_form})
