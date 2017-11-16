from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process_registration$', views.process_registration),
    url(r'^process_login$', views.process_login),
    url(r'^books$', views.show_user_reviews),
    url(r'^books/(?P<book_id>\d+)$', views.show_book_reviews),
    url(r'^add_book_review$', views.add_book_review),
    url(r'^post_book_review$', views.post_book_review),
    url(r'^logout$', views.logout),

]
