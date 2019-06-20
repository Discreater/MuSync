from django.urls import path
from . import views

urlpatterns = [
    path('current/change_time', views.change_current_time, name='change_current_time'),
    path('current/delete', views.delete_by_order, name='delete_by_order'),
    path('current/next', views.add_to_next_play, name='add_to_next_play'),
    path('current/all', views.get_current_list, name='get_current_track'),
    path('current/play', views.play, name='play'),
    path('current/pause', views.pause, name='pause'),
    path('current/play-now', views.play_now, name='play_now'),
]
