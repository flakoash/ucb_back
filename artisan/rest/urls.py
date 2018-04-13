from django.conf.urls import include, url
from . import views
urlpatterns = [
    url(r'^api/XOXOXO/$', views.XOXOXOView.as_view()),
    url(r'^api/XOXOXO/(?P<pk>[0-9]+)/$', views.XOXOXODetailView.as_view()),
]