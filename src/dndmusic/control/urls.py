

from django.urls import include, path
from dndmusic.control.views.home import MainPage
from dndmusic.control.views import home
urlpatterns = [
    path('home', home.MainPage.as_view(),name='home')
]
