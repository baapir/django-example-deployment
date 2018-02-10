from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def test(request):
    return HttpResponse("its a test view!!from django_level_four.views!!")


def index(request):
    return render(request, 'django_level_four/indexpage.html', {'number': 123, 'data': 'filter'})


def secondindex(request):
    return render(request, 'django_level_four/secondindex.html')


def thirdindex(request):
    return render(request, 'django_level_four/thirdindex.html')

