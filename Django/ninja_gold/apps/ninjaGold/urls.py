from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^ninja_gold$',views.index),
    url(r'^process_money/(?P<building>\w+)$',views.process_money),
    url(r'^reset$',views.reset_session),
]
