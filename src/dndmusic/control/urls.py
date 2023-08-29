

from django.urls import path
from dndmusic.control.views import home
urlpatterns = [
    path('home', home.MainPage.as_view(),name='home')
]
