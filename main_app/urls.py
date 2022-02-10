from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"), # <- new route
    path('songs/', views.SongList.as_view(), name="song_list"),
    path('songs/new/', views.SongCreate.as_view(), name="song_create"),
    path('songs/<int:pk>/', views.SongDetail.as_view(), name="song_detail"),
    path('songs/<int:pk>/update',views.SongUpdate.as_view(), name="song_update"),
    path('songs/<int:pk>/delete',views.SongDelete.as_view(), name="song_delete"),
]