from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.contrib.auth import authenticate, login

from django.views.generic import ListView
from dndmusic.base.models.tagging import Tag
from django.shortcuts import render, redirect
from dndmusic.control.forms.login import LoginForm

class TagOverview(View, LoginRequiredMixin):
    def get(self, request):
        user = request.user
        tags=Tag.objects.all()
        context={'tags':tags,
                 'user':user
        }
        return render(request,'control/tagging/tag_overview.html',context=context)


class NewTag(View, LoginRequiredMixin):
    def get(self, request):
        user = request.user
        context={'user':user
        }
        return render(request,'control/tagging/new_tag.html',context=context)
    

class NewScale(View, LoginRequiredMixin):
    def get(self, request):
        user = request.user
        context={'user':user
        }
        return render(request,'control/tagging/new_scale.html',context=context)
    
    