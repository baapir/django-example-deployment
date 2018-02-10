from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("its first view at all")

def secondindex(request):
    return HttpResponse("<em> this is second view with em html tag </em>")

def temp_first_page(request):
    return render(request, 'django_level_one/firsttemp.html', {'inject_me': 'hello im from views.Temp_first_page'})