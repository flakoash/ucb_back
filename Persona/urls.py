from django.conf.urls import include, url
from . import views
urlpatterns = [
    url(r'^api/Persona/$', views.PersonaView.as_view()),
    url(r'^api/Persona/profileph/$', views.imageUpload.as_view()),
    url(r'^api/Persona/(?P<pk>\w+|[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$', views.PersonaDetailView.as_view()),
]