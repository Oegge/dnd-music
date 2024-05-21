from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.contrib.auth import authenticate, login

from django.views.generic import ListView
from dndmusic.base.models.playlist import Playlist
from dndmusic.base.models.song import Song
from django.shortcuts import render, redirect
from dndmusic.control.forms.login import LoginForm


class DnDView(View, LoginRequiredMixin):
    pass


class Login(View):
    def get(self, request):
        # Check if the user is already authenticated
        if request.user.is_authenticated:
            return redirect("control:home")
            
        form = LoginForm()
        return render(request, "control/login.html", {"form": form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                return redirect("control:home")
        else:
            # Return the form with the validation errors
            return render(request, "control/login.html", {"form": form})


class LandingPage(View, LoginRequiredMixin):
    def get(self, request, user_id):
        # Check if the user is already authenticated
        if request.user.is_authenticated:
            return redirect("control:home")
            
        form = LoginForm()
        return render(request, "control/login.html", {"form": form})


class MainPage(View, LoginRequiredMixin):
   
    template_name = "control/home.html"

    def get(self, request):
        user = request.user
        recent_songs = user.uploaded_songs.all().order_by('-last_played')[:5]  # Get the last 5 played songs
        playlists = Playlist.objects.all()  # Get the last 5 played songs
        context = {'recent_songs': recent_songs,"playlists":playlists}

        return render(request, self.template_name,context=context )


class Songs(View, LoginRequiredMixin):
    def get(self, request):
        user = request.userzz
        songs=Song.objects.all()
        context={'songs':songs,

        }
        return render(request,'control/songs/song_overview.html',context=context)