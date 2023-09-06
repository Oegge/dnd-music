from django.urls import path
from dndmusic.control.views import home
from dndmusic.control.views import songs
from dndmusic.control.views import playlists
from dndmusic.control.views import tagging
urlpatterns = [
    path('login', home.Login.as_view(),name='login'),
    path('home', home.MainPage.as_view(),name='home'),
    path('songs/overview', songs.SongOverview.as_view(),name='songs.overview'),
    path('songs/add', songs.AddSong.as_view(), name='songs.add'),
    path('playlists/overview', playlists.PlaylistOverview.as_view(), name='playlists.overview'),
    path('playlists/new', playlists.NewPlaylist.as_view(), name='playlists.new'),
    path('playlists/<int:playlist_id>/edit', playlists.EditPlaylist.as_view(), name='playlists.edit'),
    path('tagging/tags/overview',tagging.TagOverview.as_view(), name='tagging.tags.overview'),
    path('tagging/tags/new',tagging.NewTag.as_view(), name='tagging.tags.new'),
    path('tagging/scales/overview',tagging.ScaleOverview.as_view(), name='tags.scales.overview'),
    path('tagging/scales/new',tagging.NewScale.as_view(), name='tagging.scales.new'),
    path('song/play/<int:song_id>',songs.PlaySong.as_view(), name='play.single.song')
    
]
