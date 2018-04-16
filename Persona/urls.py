from django.conf.urls import include, url
from . import views
urlpatterns = [
    url(r'^api/Persona/$', views.PersonaView.as_view()),
    url(r'^api/Persona/(?P<pk>[0-9]+)/$', views.PersonaDetailView.as_view()),
]