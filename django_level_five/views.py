from django.shortcuts import render
from . import forms
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout


# Create your views here.
##reversees not working
def test(request):
    return render(request, 'django_level_five/test.html')


def index(request):
    return render(request, 'django_level_five/index.html')


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = forms.UserForm(request.POST)
        profile_form = forms.UserProfileInfoForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            ##one to one field
            profile.user = user

            ##for savin pic
            if 'profile_pic' in request.files:
                profile.profile_pic = request.files['profile_pic']

            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = forms.UserForm()
        profile_form = forms.UserProfileInfoForm()
    return render(request, 'django_level_five/registrations.html',
                  {'uform': user_form,
                   'upform': profile_form,
                   'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')##name of textfield in html
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('django_level_five/index.html'))
            else:
                return HttpResponse("Your acount isnt active ")
        else:
            print("some one try to login and failed ")
            print("usrname:{} and password:{}".format(username, password))
            return HttpResponse("invalid login detail suplide")
    return render(request, 'django_level_five/login.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('django_level_five/index.html'))


@login_required
def special(request):
    return HttpResponse('you are special!!!')