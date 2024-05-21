# dndmusic/control/rest/controller/api_controller.py

import json
from dndmusic.base.models.playlist import Playlist
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from dndmusic.base.models import Song
from dndmusic.control.serializer import SongSerializer  # Correct import path

@api_view(['POST'])
def update_song_order(request):
    print(request.data)
    order_data = request.data.get('order[]')
    print(order_data)
    order_list = order_data.split(',')
    print(order_list)
    order = [int(item) for item in order_list]

    playlist_id = request.data.get('playlist')
    if order_data is None:
        return Response({'error': 'Order data is missing'}, status=status.HTTP_400_BAD_REQUEST)
    playlist = Playlist.objects.get(id=playlist_id)
    playlist.song_ids_ordered = order
    playlist.save()

    return Response({'status': 'success'}, status=status.HTTP_200_OK)
