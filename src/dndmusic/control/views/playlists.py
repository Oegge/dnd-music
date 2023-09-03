from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.contrib.auth import authenticate, login

from django.views.generic import ListView
from dndmusic.base.models.playlist import Playlist
from django.shortcuts import render, redirect
from dndmusic.control.forms.login import LoginForm


class PlaylistOverview(View, LoginRequiredMixin):
    def get(self, request):
        user = request.user
        playlists=Playlist.objects.all()
        context={'playlists':playlists,
                 'user':user
        }
        return render(request,'control/songs/song_overview.html',context=context)
