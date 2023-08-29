from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView
from dndmusic.base.models.song import Song
from django.shortcuts import render, redirect


class MainPage(View):
    template_name='control/home.html'
    def get(self, request):
        return render(request,self.template_name,context={})
    pass

class ListSongs(ListView,LoginRequiredMixin,):
    model=Song
    template_name='test.html'
    context_object_name='Songs'
    paginate_by=10