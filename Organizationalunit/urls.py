from django.conf.urls import include, url
from . import views
urlpatterns = [
    url(r'^api/Organizationalunit/$', views.OrganizationalunitView.as_view()),
    url(r'^api/Organizationalunit/(?P<pk>[0-9]+)/$', views.OrganizationalunitDetailView.as_view()),
]