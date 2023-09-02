

from django.urls import path
from dndmusic.control.views import home
urlpatterns = [
    path('login', home.Login.as_view(),name='login'),
    path('home', home.MainPage.as_view(),name='home'),
    path('', home.LandingPage.as_view(),name='')
]
