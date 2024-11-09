from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.contrib.auth import authenticate, login

from django.views.generic import ListView
from dndmusic.base.models.song import Song
from django.shortcuts import render, redirect
from dndmusic.base.models.tagging import Tag
from dndmusic.control.forms.SongTagsForm import SongTagsForm
from dndmusic.control.forms.login import LoginForm
from dndmusic.control.forms.BulkUploadForm import BulkUploadForm


class SongOverview(View, LoginRequiredMixin):
    def get(self, request):
        user = request.user
        songs = Song.objects.all()
        context = {'songs': songs,
                   'user': user,
                   }
        return render(request, 'control/songs/song_overview.html', context=context)


class AddSong(View, LoginRequiredMixin):
    def get(self, request):
        user = request.user
        context = {'user': user
                   }
        return render(request, 'control/songs/add_song.html', context=context)


class PlaySong(View, LoginRequiredMixin):
    def get(self, request, song_id):
        songs = Song.objects.all()
        context = {'songs': songs}
        return render(request, 'control/songs/all_songs.html', context=context)


class PlaySongs(View, LoginRequiredMixin):
    def get(self, request):
        songs = Song.objects.all()
        form = SongTagsForm()
        all_tags = Tag.objects.all()
        context = {'songs': songs, 'form': form, 'all_tags': all_tags}
        return render(request, 'control/songs/all_songs.html', context=context)


class BulkAddSongsView(View, LoginRequiredMixin):
    template_name = 'control/songs/bulk_add_songs.html'

    def get(self, request):
        form = BulkUploadForm()
        tags = Tag.objects.all()
        return render(request, self.template_name, {'form': form, 'tags': tags})

    def post(self, request):
        form = BulkUploadForm(request.POST, request.FILES)
        print(request.POST)
        tags = list(Tag.objects.all())
        if form.is_valid():
            files = request.FILES.getlist('audio_files')
            for i, f in enumerate(files):
                try:
                    name = request.POST[f"song_name_{i}"]
                except:
                    name = f.name
                song = Song(audio=f, name=name, uploader=request.user)
                song.save()

                try:
                    tags = request.POST[f'tags_{i}']
                    song.tags.set(Tag.objects.filter(id__in=tags))
                    song.save()
                except:
                    song.tags.set(Tag.objects.filter(id=1))
                    song.save()

            return redirect(reverse('control:songs.overview'))  # Redirect to a success page or similar
        return render(request, self.template_name, {'form': form})
