from django.conf.urls import url
from . import views

app_name = 'django_level_five'

urlpatterns = [
    url(r'^$', views.test),
    url(r'^register/$', views.register, name='register'),
    url(r'^index/$', views.index, name='index'),
    url(r'^user_login/$', views.user_login, name='user_login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^special/$', views.special, name='special'),
]