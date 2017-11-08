from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^/new$', views.register),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
]
