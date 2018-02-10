from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index),
    url(r'test/$', views.secondindex),
    url(r'temp/$', views.temp_first_page),
]