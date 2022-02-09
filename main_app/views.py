from django.shortcuts import render
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
from django.views.generic.base import TemplateView
from .models import Songs
# Create your views here.

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

songs = [
  Songs("Sweet Jane", "https://hips.hearstapps.com/esq.h-cdn.co/assets/cm/15/06/54d1ede2a7224_-_esq-102813-lou-reed-2.jpg",
          "Lorem ipsum dolor sit amet, consectetur adipiscing elit."),
  Songs("Who Loves the Sun", "https://variety.com/wp-content/uploads/2019/10/2019_1599_004-e1572475947414.jpg?w=681&h=383&crop=1", "Sed varius in sem convallis rutrum."),
  Songs("Oh! Sweet Nuthin'", "https://www.telegraph.co.uk/content/dam/books/2017/12/28/TELEMMGLPICT000149622020_trans_NvBQzQNjv4BqplGOf-dgG3z4gg9owgQTXDVXE4-NcPVfcZy5a1cUJ04.jpeg?imwidth=680", "Curabitur ut ultrices neque."),
]

class SongList(TemplateView):
    template_name = "song_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["song"] = songs # this is where we add the key into our context object for the view to use
        return context