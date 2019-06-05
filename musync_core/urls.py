from django.urls import path
from . import views

urlpatterns = [
    # ex: /musync/
    path('', views.index, name='index'),
    # ex: /musync/5/
    path('<int:song_id>/', views.detail, name='detail'),
    # ex: /musync/5/results/
    path('<int:song_id>/results/', views.results, name='results'),
    # ex: /musync/5/vote/
    path('<int:song_id>/vote/', views.vote, name='vote'),
]