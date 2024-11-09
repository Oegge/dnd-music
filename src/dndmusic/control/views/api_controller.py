import json

from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from dndmusic.base.models import Song, Tag, Playlist
from dndmusic.control.serializer import SongTagsSerializer


@api_view(['POST'])
def update_song_order(request):
    order_data = request.data.get('order[]')
    order_list = order_data.split(',')
    order = [int(item) for item in order_list]
    playlist_id = request.data.get('playlist')
    if order_data is None:
        return Response({'error': 'Order data is missing'}, status=status.HTTP_400_BAD_REQUEST)
    playlist = Playlist.objects.get(id=playlist_id)
    playlist.song_ids_ordered = order
    playlist.save()

    return Response({'status': 'success'}, status=status.HTTP_200_OK)


@api_view(['POST'])
def update_tags(request, song_id):
    song = Song.objects.get(pk=song_id)
    serializer = SongTagsSerializer(song)

    tag_ids = request.data.getlist('tags')  # This fetches all 'tags' entries as a list of strings
    tags = Tag.objects.filter(id__in=tag_ids)
    song.tags.set(tags)
    song.save()
    return Response(serializer.data, status=200)


@api_view(["DELETE"])
def delete_playlist(request, pk):
    try:
        playlist = Playlist.objects.get(pk=pk)
        playlist.delete()
        return JsonResponse({'message': 'Playlist deleted successfully.'}, status=204)
    except Playlist.DoesNotExist:
        return JsonResponse({'error': 'Playlist not found.'}, status=404)


@api_view(["GET"])
def update_durations(request):
    try:
        songs = Song.objects.all()
        for song in songs:
            song.save()
        return JsonResponse({'message': 'durations updates successfully.'}, status=202)
    except Playlist.DoesNotExist:
        return JsonResponse({'error': 'Playlist not found.'}, status=404)

@api_view(["GET"])
def get_song_tags(request):
    try:
        songs = Song.objects.all()
        song_with_tags = []

        for song in songs:
            tags = [tag.name for tag in song.tags.all()]  # Assuming tags have a 'name' field
            song_with_tags.append({
                'song_title': song.name,  # Assuming 'title' field for Song
                'tags': tags
            })

        return JsonResponse(song_with_tags, safe=False, status=202)
    except Song.DoesNotExist:
        return JsonResponse({'error': 'Songs not found.'}, status=404)