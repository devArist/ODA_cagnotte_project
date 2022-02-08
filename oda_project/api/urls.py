from django.urls import path
from . import apiviews

from . import views

urlpatterns = [
    path("", apiviews.home, name="home"),
    path("academicians/", apiviews.api_academicians, name="academicians"),
    path('academicians/<int:pk>', apiviews.api_academician, name='academician')
]
