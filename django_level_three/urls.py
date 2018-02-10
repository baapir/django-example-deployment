from django.conf.urls import url
from django_level_three import views


urlpatterns = [
    url(r'^$', views.indextest),
    url(r'^testform/$', views.testform),
    url(r'^signup/$', views.signup),
]