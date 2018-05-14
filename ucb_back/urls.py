"""ucb_back URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

from django.views import generic
from rest_framework.schemas import get_schema_view
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', generic.RedirectView.as_view(url='/api/', permanent=False)),
    url(r'^api/$', get_schema_view()),
    url(r'^api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/auth/token/obtain/$', TokenObtainPairView.as_view()),
    url(r'^api/auth/token/refresh/$', TokenRefreshView.as_view()),
    url('', include('Unidadorganigrama.urls')), 
    url('', include('Persona.urls')), 
    url('', include('Unidadorganizacional.urls')), 
    url('', include('Nivel.urls')),
    url('', include('Cargo.urls')), 
    url('', include('Regional.urls')),
    url('', include('Catalogodatos.urls')), 
    url('', include('Performancearea.urls')), 
    url('', include('Organizationalchartunit.urls')), 
    url('', include('Organizationalunit.urls')), 
    url('', include('Level.urls')), 
    url('', include('Position.urls')), 
    url('', include('Contract.urls')), 
    url('', include('Catalogue.urls')), 
    url('', include('Person.urls')), 
 ]