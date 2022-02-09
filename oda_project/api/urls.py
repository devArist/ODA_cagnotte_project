from django.urls import path
from . import apiviews

from . import views

urlpatterns = [
    path("", apiviews.home, name="home"),
    path("academicians/", apiviews.api_academicians, name="academicians"),
    path('academicians/<str:registration_number>', apiviews.api_academician, name='academician'),
    path('academicians/<str:registration_number>/payment/', apiviews.api_payment, name='payment')
]
