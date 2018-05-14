from django.conf.urls import include, url
from . import views
urlpatterns = [
    url(r'^api/Regional/$', views.RegionalView.as_view()),
    url(r'^api/Regional/(?P<pk>[0-9]+)/$', views.RegionalDetailView.as_view()),
]