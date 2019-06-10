from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('registerApi', views.registerApi, name='registerApi'),
    path("registerPage", views.registerPage, name='registerPage'),
    path("hello", views.hello, name='hello'),
]
