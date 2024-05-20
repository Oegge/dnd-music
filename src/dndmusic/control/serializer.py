# dndmusic/control/rest/serializers.py

from rest_framework import serializers
from dndmusic.base.models import Song

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'name', 'audio', 'order']
