from django.conf.urls import url

from . import views

app_name = 'shortener'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^link$', views.link, name='link'),

    # We do not apply bounds on the length of shortened urls because those can
    # be changed without cleaning the database. We'll simply check if the link
    # exists in the database without caring about its length.
    url(r'^!(?P<shortened_url>.+)$', views.preview, name='preview'),
    url(r'^(?P<shortened_url>.+)$', views.shortened, name='shortened'),

]
