from django.conf.urls import include, url
from . import views
urlpatterns = [
    url(r'^api/Unidadorganigrama/$', views.UnidadorganigramaView.as_view()),
    url(r'^api/Unidadorganigrama/(?P<pk>[0-9]+)/$', views.UnidadorganigramaDetailView.as_view()),
]