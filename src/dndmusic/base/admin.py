from django.contrib import admin
from dndmusic.base.models import song,tagging,playlist
# Register your models here.
admin.site.register(song.Song)
admin.site.register(tagging.Tag)
admin.site.register(playlist.Playlist)
