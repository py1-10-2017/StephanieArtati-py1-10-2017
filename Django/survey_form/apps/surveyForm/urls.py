from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process_form$', views.process_form),
    url(r'^result$', views.result)
]
