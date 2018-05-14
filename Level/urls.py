from django.conf.urls import include, url
from . import views
urlpatterns = [
    url(r'^api/Level/$', views.LevelView.as_view()),
    url(r'^api/Level/(?P<pk>[0-9]+)/$', views.LevelDetailView.as_view()),
]