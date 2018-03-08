from django.conf.urls import  include, url
from . import views
urlpatterns = [
    url('XOXOXO/index', views.index, name='index_XOXOXO'),
    url('XOXOXO/create', views.create, name='create_XOXOXO'),
    url('XOXOXO/(?P<id>\d+)', views.show, name='show_XOXOXO'),
    url('XOXOXO/delete/(?P<id>\d+)', views.delete, name='delete_XOXOXO'),
    url('XOXOXO/update/(?P<id>\d+)', views.update, name='update_XOXOXO'),
]

