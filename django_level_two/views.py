from django.shortcuts import render
from django.http import HttpResponse
from .models import AccessRecord, Topic, Webpage, UserAdded
# Create your views here.
def indextest(request):
    return HttpResponse("hello im for test.i come from django_level_two.views")


def show_all_user(request):
    all_data = AccessRecord.objects.order_by('date')
    return render(request, 'django_level_two/show_all_user.html', {'acc_record': all_data})

def show_all_userAdded(request):
    all_data = UserAdded.objects.order_by('LastName')
    return render(request, 'django_level_two/exercise.html', {'all_user_info': all_data})


