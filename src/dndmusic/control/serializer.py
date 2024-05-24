# dndmusic/control/rest/serializers.py

from dndmusic.base.models.tagging import Tag
from rest_framework import serializers
from dndmusic.base.models import Song

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'name', 'audio', 'order']
        
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id','name']
            
class SongTagsSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=False)

    class Meta:
        model = Song
        fields = ['tags']

    def create(self, validated_data):
        tags_data = validated_data.pop('tags', [])
        song = Song.objects.create(**validated_data)
        for tag_data in tags_data:
            tag, created = Tag.objects.get_or_create(**tag_data)
            song.tags.add(tag)
        return song

    def update(self, instance, validated_data):
        tags_data = validated_data.pop('tags', [])
        instance.tags.clear()  # Remove existing tags if needed
        for tag_data in tags_data:
            tag, created = Tag.objects.get_or_create(**tag_data)
            instance.tags.add(tag)
        return instance

        
