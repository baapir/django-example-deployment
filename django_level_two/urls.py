from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.indextest),
    url(r'showalldata/$', views.show_all_user),
    url(r'showalluser/$', views.show_all_userAdded)
]