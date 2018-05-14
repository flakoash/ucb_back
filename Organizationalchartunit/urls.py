from django.conf.urls import include, url
from . import views
urlpatterns = [
    url(r'^api/Organizationalchartunit/$', views.OrganizationalchartunitView.as_view()),
    url(r'^api/Organizationalchartunit/(?P<pk>[0-9]+)/$', views.OrganizationalchartunitDetailView.as_view()),
]