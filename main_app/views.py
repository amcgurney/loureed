# This will import the class we are extending 
from django.views.generic.edit import CreateView, UpdateView

from django.shortcuts import render
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
from django.views.generic.base import TemplateView
from .models import Songs
# Create your views here.
from django.views.generic import DetailView

# Here we will be creating a class called Home and extending it from the View class
class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

    # Here we are adding a method that will be ran when we are dealing with a GET request
    def get(self, request):
        # Here we are returning a generic response
        # This is similar to response.send() in express
        return HttpResponse("Lou Reed Home")

class About(View):

    def get(self, request):
        return HttpResponse("Lou Reed About")

# songs = []

class SongList(TemplateView):
    template_name = "song_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["songs"] = Songs.objects.all() # this is where we add the key into our context object for the view to use
        context["header"] = "Trending Songs"
        return context

class SongCreate(CreateView):
    model = Songs
    fields = ['name', 'img', 'bio']
    template_name = "song_create.html"
    success_url = "/songs/"

class SongDetail(DetailView):
    model = Songs
    template_name = "song_detail.html"

class SongUpdate(UpdateView):
    model = Songs
    fields = ['name', 'img', 'bio']
    template_name = "song_update.html"
    success_url = "/artists/"