from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

from django.views.generic import ListView
from dndmusic.base.models.song import Song
from django.shortcuts import render, redirect

class DnDView(View,LoginRequiredMixin):
    pass

class LandingPage(DnDView):
    def get(self, request):
        return redirect(reverse('control:home'))

class MainPage(DnDView):
    
    template_name='control/home.html'
    
    def get(self, request):
        return render(request,self.template_name,context={})
