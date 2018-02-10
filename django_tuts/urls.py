"""django_tuts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^djangolevelone/', include('django_level_one.urls')),
    url(r'^djangoleveltwo/', include('django_level_two.urls')),
    url(r'^djangolevelthree/', include('django_level_three.urls')),
    url(r'djangolevelfour/', include('django_level_four.urls')),
    url(r'^djangolevelfive/', include('django_level_five.urls')),
]
