"""eSign_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from eSignApp import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^sign_up/', views.sign_up),
    url(r'^sign_in/', views.sign_in),
    url(r'^upload/', views.upload),
    url(r'^get_details/', views.get_details),
    url(r'^get_images/', views.get_images),
    url(r'^send_mail/', views.send_email),
    url(r'^change_password/', views.change_password),
    url(r'^get_default_image/', views.get_default_image),
    url(r'^set_default_image/', views.set_default_image),
    url(r'^edit_details/', views.edit_details),
    url(r'^get_default_preffered_name/', views.get_default_preffered_name),
    url(r'^drop/', views.erase)
]