from django.urls import path
from dndmusic.control.views.api_controller import update_song_order, update_tags, update_durations, get_song_tags
from dndmusic.control.views import api_controller
from dndmusic.control.views import home
from dndmusic.control.views import songs
from dndmusic.control.views import playlists
from dndmusic.control.views import tagging
from django.views.generic.base import RedirectView


urlpatterns = [

    path("login", home.Login.as_view(), name="login"),
    path("home", home.MainPage.as_view(), name="home"),
    path("", RedirectView.as_view(url="/home", permanent=False), name="index"),

    path("playlists/overview", playlists.PlaylistOverview.as_view(), name="playlists.overview"),
    path("playlists/new", playlists.NewPlaylist.as_view(), name="playlists.new"),
    path("playlist/<int:playlist_id>/edit", playlists.EditPlaylist.as_view(), name="playlists.edit" ),
    path("playlist/<int:pk>", playlists.ShowPlaylist.as_view(), name="playlist-detail"),

    path("update_order/", playlists.UpdatePlaylist.as_view(), name="UpdatePlaylist"),
    path("tagging/tags/overview", tagging.TagOverview.as_view(), name="tagging.tags.overview"),

    path("tagging/tags/new", tagging.NewTag.as_view(), name="tagging.tags.new"),
    path("tagging/scales/new", tagging.NewScale.as_view(), name="tagging.scales.new"),

    path("songs/overview", songs.SongOverview.as_view(), name="songs.overview"),
    path("songs/play", songs.PlaySongs.as_view(), name="play.single.song"),
    path("songs/add", songs.BulkAddSongsView.as_view(), name="songs.add"),
    path('add_bulk_songs/', songs.BulkAddSongsView.as_view(), name='add_bulk_songs'),

    path("edit/tag/<int:song_id>", update_tags, name="update_order"),

    path('delete/playlist/<int:pk>/', api_controller.delete_playlist, name='playlist-delete'),
    path("api/update_order/", update_song_order, name="update_order"),
    path("api/update_durations", update_durations, name="update_durations"),
    path("api/get_song_tags", get_song_tags, name="get_song_tags"),
]




