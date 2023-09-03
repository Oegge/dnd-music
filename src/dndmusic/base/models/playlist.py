from django.db import models
from dndmusic.base.models.song import Song


class Playlist(models.Model):
    name = models.CharField(max_length=100)
    songs = models.ManyToManyField(Song, related_name="playlists")

    def add_song(self, song:Song):
        if not song in self.songs.all():
            self.songs.add(song)

    def _is_duplicate_song_(self, song:Song) -> bool:
        return song in self.songs.all()
    
    def remove_song(self, song:Song):
        self.songs.remove(song)
