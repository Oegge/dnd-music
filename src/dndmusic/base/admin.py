from django.contrib import admin
from dndmusic.base.models import song,tagging
# Register your models here.
admin.site.register(song.Song)
admin.site.register(tagging.Scale)
admin.site.register(tagging.Tag)
