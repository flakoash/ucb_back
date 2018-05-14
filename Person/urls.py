from django.conf.urls import include, url
from . import views
urlpatterns = [
    url(r'^api/Person/$', views.PersonView.as_view()),
    url(r'^api/Person/(?P<pk>[0-9]+)/$', views.PersonDetailView.as_view()),
]