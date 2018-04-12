from django.conf.urls import  include, url
from . import views
urlpatterns = [
    url(r'^index$', views.index, name='index_XOXOXO'),
    url(r'^create$', views.create, name='create_XOXOXO'),
    url(r'^(?P<id>\d+)$', views.show, name='show_XOXOXO'),
    url(r'^delete/(?P<id>\d+)$', views.delete, name='delete_XOXOXO'),
    url(r'^update/(?P<id>\d+)$', views.update, name='update_XOXOXO'),
]

