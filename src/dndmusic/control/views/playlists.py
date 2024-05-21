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
        playlist=Playlist.objects.get(id=pk)
        songs = playlist.get_ordered_songs()
        print(playlist)
        context = {"songs": songs, "playlist":playlist,"user": user}
        return render(
            request, "control/playlists/playlist.html", context=context
        )
        
class PlaylistDJ(View, LoginRequiredMixin):
    def get(self, request):
        user = request.user
        playlists=Playlist.objects.all()
        songs = {playlist.id :playlist.get_ordered_songs() for playlist in playlists}
        context = {"songs": songs, "playlists":playlists,"user": user}
        return render(
            request, "control/playlists/DJ.html", context=context
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
        song_ids = request.POST.getlist('song_ids[]')
        try:
            song_ids = [int(song_id) for song_id in song_ids]
        except ValueError:
        # Handle the error if conversion fails
            song_ids = []
        print(song_ids)
        
        if song_ids is not None:
            print(song_ids)
            songs = Song.objects.filter(id__in=song_ids)
            playlist = Playlist()
            playlist.save()
            playlist.name = request.POST.get('name')
            playlist.songs.set(songs)
            playlist.song_ids_ordered = song_ids
            playlist.save()
            
            user = request.user
            return redirect('control:playlist-detail', pk=playlist.pk) 
        user = request.user
        songs = Song.objects.all()
        context = {"user": user,'songs':songs}
        return render(request, "control/playlists/new_playlist.html", context=context)

   
class UpdatePlaylist(View, LoginRequiredMixin):
    def get(self, request):
        user = request.user
        context = {"user": user}
        return render(request, "control/playlists/new_playlist.html", context=context)
    
    def post(self, request):
        print(request.POST)
        
        return 
        
    