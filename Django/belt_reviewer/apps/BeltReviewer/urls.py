from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process_registration$', views.process_registration),
    url(r'^process_login$', views.process_login),
    url(r'^books$', views.show_reviews),
    url(r'^books/(?P<book_id>\d+)$', views.show_book_reviews),
    url(r'^books/(?P<book_id>\d+)/add_review$', views.add_review_to_book),
    url(r'^add_book_review$', views.add_book_review),
    url(r'^post_book_review$', views.post_book_review),
    url(r'^reviews/(?P<review_id>\d+)/delete$', views.delete_review),
    url(r'^users/(?P<user_id>\d+)$', views.show_user),
    url(r'^logout$', views.logout),

]
