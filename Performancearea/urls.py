from django.conf.urls import include, url
from . import views
urlpatterns = [
    url(r'^api/Performancearea/$', views.PerformanceareaView.as_view()),
    url(r'^api/Performancearea/(?P<pk>[0-9]+)/$', views.PerformanceareaDetailView.as_view()),
]