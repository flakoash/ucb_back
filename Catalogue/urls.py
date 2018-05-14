from django.conf.urls import include, url
from . import views
urlpatterns = [
    url(r'^api/Catalogue/$', views.CatalogueView.as_view()),
    url(r'^api/Catalogue/(?P<pk>[0-9]+)/$', views.CatalogueDetailView.as_view()),
]