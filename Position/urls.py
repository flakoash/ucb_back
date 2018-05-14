from django.conf.urls import include, url
from . import views
urlpatterns = [
    url(r'^api/Position/$', views.PositionView.as_view()),
    url(r'^api/Position/(?P<pk>[0-9]+)/$', views.PositionDetailView.as_view()),
]