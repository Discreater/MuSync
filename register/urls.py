from django.urls import path
from . import views

urlpatterns = [
    path('registerApi', views.registerApi, name='registerApi'),
    path("registerPage", views.registerPage, name='registerPage'),
    path("hello", views.hello, name='hello'),
]
