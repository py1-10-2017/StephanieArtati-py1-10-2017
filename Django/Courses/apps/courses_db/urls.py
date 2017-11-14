from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^courses$', views.index),
    url(r'^courses/(?P<course_id>\d+)/destroy_confirm$', views.destroy_confirm),
    url(r'^courses/(?P<course_id>\d+)/destroy$', views.destroy),
    url(r'^courses/add$', views.add_course),
]
