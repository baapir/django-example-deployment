from django.shortcuts import render
from django.http import HttpResponse
from . import forms
# Create your views here.


def indextest(request):
    return HttpResponse('this is http response for testing django level three app firs url')


def testform(requst):
    form = forms.testform

    if requst.method == 'POST':
        form = forms.testform(requst.POST)

        if form.is_valid():
            print('validaton seccess!!')
            print('name: ' + form.cleaned_data['name'])
            print('Email: ' + form.cleaned_data['email'])
            print('Text: ' + form.cleaned_data['text'])

    return render(requst, 'django_level_three/testform.html', {'form': form})

def signup(request):
    form = forms.signupssform()

    if request.method == 'POST':
        form = forms.signupssform(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return render(request, 'django_level_three/success.html')
        else:
            print('Erroe!! form is invalid!!!')

    return render(request, 'django_level_three/signup.html', {'form': form})

