from django.urls import path
from . import apiviews

from . import views

urlpatterns = [
    path("", apiviews.home, name="home"),
    path("academicians/", apiviews.api_academicians, name="api_academicians"),
    ]


