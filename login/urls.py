from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('<int:user_id>/fetch-info', views.fetch_info, name='fetch-info'),
    path('change-info', views.change_info, name='change-info'),
]
