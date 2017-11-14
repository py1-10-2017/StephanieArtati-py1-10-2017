from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^users$', views.index),
    url(r'^users/new$', views.new),
    url(r'^users/create$', views.create),
    url(r'^users/(?P<user_id>\d+)$', views.show_and_update),
    url(r'^users/(?P<user_id>\d+)/destroy$', views.destroy),
    url(r'^users/(?P<user_id>\d+)/edit$', views.edit),
]
