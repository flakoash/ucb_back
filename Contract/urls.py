from django.conf.urls import include, url
from . import views
urlpatterns = [
    url(r'^api/Contract/$', views.ContractView.as_view()),
    url(r'^api/Contract/(?P<pk>[0-9]+)/$', views.ContractDetailView.as_view()),
]