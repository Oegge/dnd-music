# dndmusic/control/rest/controller/api_controller.py

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from dndmusic.base.models import Song
from dndmusic.control.serializer import SongSerializer  # Correct import path

@api_view(['POST'])
def update_song_order(request):
    print(request.data)
    order_data = request.data.get('order[]')
    if order_data is None:
        return Response({'error': 'Order data is missing'}, status=status.HTTP_400_BAD_REQUEST)

    for index, song_id in enumerate(order_data):
        try:
            song = Song.objects.get(id=song_id)
            song.order = index
            song.save()
        except Song.DoesNotExist:
            return Response({'error': f'Song with id {song_id} does not exist'}, status=status.HTTP_400_BAD_REQUEST)

    return Response({'status': 'success'}, status=status.HTTP_200_OK)
