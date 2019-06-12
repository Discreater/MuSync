from django.urls import path
from . import views


urlpatterns = [
    path('<int:user_id>/friends/', views.get_friends, name='get_friends'),
]