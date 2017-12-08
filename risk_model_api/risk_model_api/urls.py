from django.conf.urls import url, include
from rest_framework import routers
from risks import views

router = routers.DefaultRouter()

urlpatterns = [
    url(r'^risks/$', views.RiskList.as_view()),
    url(r'^risks/(?P<pk>[0-9]+)/$', views.RiskDetail.as_view()),
]
