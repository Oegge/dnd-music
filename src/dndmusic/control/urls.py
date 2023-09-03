from django.urls import path
from dndmusic.control.views import home
from dndmusic.control.views import songs
from dndmusic.control.views import playlists

urlpatterns = [
    path('login', home.Login.as_view(),name='login'),
    path('home', home.MainPage.as_view(),name='home'),
    path('songs/overview', songs.SongOverview.as_view(),name='songs.overview'),
    path('playlists/overview', playlists.PlaylistOverview.as_view(), name='playlists.overview')

]
