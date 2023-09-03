from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.contrib.auth import authenticate, login

from django.views.generic import ListView
from dndmusic.base.models.song import Song
from django.shortcuts import render, redirect
from dndmusic.control.forms.login import LoginForm


class SongOverview(View, LoginRequiredMixin):
    def get(self, request):
        user = request.user
        songs=Song.objects.all()
        context={'songs':songs,
                 'user':user
        }
        return render(request,'control/songs/song_overview.html',context=context)
    

class AddSong(View, LoginRequiredMixin):
    def get(self, request):
        user = request.user
        context={'user':user
        }
        return render(request,'control/songs/add_song.html',context=context)    