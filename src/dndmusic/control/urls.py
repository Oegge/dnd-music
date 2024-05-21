from django.urls import path
from dndmusic.control.views.api_controller import update_song_order
from dndmusic.control.views import home
from dndmusic.control.views import songs
from dndmusic.control.views import playlists
from dndmusic.control.views import tagging
from django.views.generic.base import RedirectView

urlpatterns = [
    path("login", home.Login.as_view(), name="login"),
    path("home", home.MainPage.as_view(), name="home"),
    path("", RedirectView.as_view(url="/home", permanent=False), name="index"),
    path("songs/overview", songs.SongOverview.as_view(), name="songs.overview"),
    path("songs/add", songs.BulkAddSongsView.as_view(), name="songs.add"),
    path(
        "playlists/overview",
        playlists.PlaylistOverview.as_view(),
        name="playlists.overview",
    ),
    path("playlists/new", playlists.NewPlaylist.as_view(), name="playlists.new"),
    path(
        "playlists/<int:playlist_id>/edit",
        playlists.EditPlaylist.as_view(),
        name="playlists.edit",
    ),
    path("update_order/", playlists.UpdatePlaylist.as_view(), name="UpdatePlaylist"),
    path("dj/", playlists.PlaylistDJ.as_view(), name="dj"),
    path(
        "tagging/tags/overview",
        tagging.TagOverview.as_view(),
        name="tagging.tags.overview",
    ),
    path("tagging/tags/new", tagging.NewTag.as_view(), name="tagging.tags.new"),
   
    path("tagging/scales/new", tagging.NewScale.as_view(), name="tagging.scales.new"),
    path("song/play/<int:song_id>", songs.PlaySong.as_view(), name="play.single.song"),
    path("api/update_order/", update_song_order, name="update_order"),
    path("playlists/<int:pk>", playlists.ShowPlaylist.as_view(), name="playlist-detail"),
    path('add_bulk_songs/', songs.BulkAddSongsView.as_view(), name='add_bulk_songs'),

]
