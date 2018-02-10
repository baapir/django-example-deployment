from django.conf.urls import url
from . import views

app_name = "django_level_four"

urlpatterns = [
    url(r'^$', views.test),
    url(r'^index/$', views.index, name='index'),
    url(r'^secondindex/$', views.secondindex, name='secondindex'),
    url(r'^thirdindex/$', views.thirdindex, name='thirdindex'),
]
