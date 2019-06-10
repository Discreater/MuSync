from django.shortcuts import render
from django.http import HttpResponse
from .models import Track


def index(request):
    hot_song_list = Track.objects.order_by('-artist_hotness')[:5]
    output = ', '.join(q.title for q in hot_song_list)
    return HttpResponse(output)


def detail(request, song_id):
    return HttpResponse("You're looking at song %s." % song_id)


def results(request, song_id):
    print(request.session.session_key)
    response = "You're looking at the results of song %s."
    return HttpResponse(response % song_id)


def vote(request, song_id):
    return HttpResponse("You're voting on question %s." % song_id)
