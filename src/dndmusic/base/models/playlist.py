import json
from typing import Iterable
from django.db import models
from dndmusic.base.models.song import Song


class Playlist(models.Model):
    name = models.CharField(max_length=100)
    songs = models.ManyToManyField(Song, related_name="playlists")
    song_ids_ordered = models.CharField(max_length=1024, default="")
    
    def get_ordered_songs(self):
        song_ids = json.loads(self.song_ids_ordered)
        if not song_ids:
            return []
        songs = list(self.songs.filter(id__in=song_ids))
        song_dict = {song.id: song for song in songs}
        
        return [song_dict[song_id] for song_id in song_ids if song_id in song_dict]
    
    def add_song(self, song:Song):
        if not song in self.songs.all():
            self.songs.add(song)

    def _is_duplicate_song_(self, song:Song) -> bool:
        return song in self.songs.all()
    
    def remove_song(self, song:Song):
        self.songs.remove(song)
        
    def __str__(self) -> str:
        return self.name
    