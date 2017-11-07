from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^session_words$', views.index),
    url(r'^process_form$', views.process_form),
    url(r'^reset$', views.reset),
    url(r'^$', views.index)
]
