from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.contrib.auth import authenticate, login

from django.views.generic import ListView
from dndmusic.base.models.playlist import Playlist
from django.shortcuts import render, redirect
from dndmusic.control.forms.login import LoginForm
from dndmusic.control.forms.AddSongForm import AddSongForm
from dndmusic.base.models.song import Song

class PlaylistOverview(View, LoginRequiredMixin):
    def get(self, request):
        user = request.user
        playlists = Playlist.objects.all()
        context = {"playlists": playlists, "user": user}
        return render(
            request, "control/playlists/playlist_overview.html", context=context
        )

class ShowPlaylist(View, LoginRequiredMixin):
    def get(self, request, pk):
        user = request.user
        playlist = Playlist.objects.get(id=pk)
        context = {"playlist": playlist, "user": user}
        return render(
            request, "control/playlists/playlist.html", context=context
        )


class EditPlaylist(View, LoginRequiredMixin):
    def get(self, request, playlist_id):
        user = request.user
        playlist = Playlist.objects.filter(id=playlist_id)
        context = {"playlist": playlist, "user": user}
        return render(request, "control/playlists/edit_playlist.html", context=context)


class NewPlaylist(View, LoginRequiredMixin):
    def get(self, request):
        user = request.user
        songs = Song.objects.all()
        context = {"user": user,'songs':songs}
        return render(request, "control/playlists/new_playlist.html", context=context)

    def post(self, request):
        form = AddSongForm(request.POST)
        user = request.user
        
        if form.is_valid():
            playlist = form.save()
            return redirect('control:playlist-detail', pk=playlist.pk) 
        context = {"user": user,'form':form}
        
        return render(request, "control/playlists/new_playlist.html", context=context)
   
class UpdatePlaylist(View, LoginRequiredMixin):
    def get(self, request):
        user = request.user
        context = {"user": user}
        return render(request, "control/playlists/new_playlist.html", context=context)
    
    def post(self, request):
        print(request.POST)
        
        return 
        
    