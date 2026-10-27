from django.urls import path

from songs.views import SongCreate
urlpatterns = [

   path("song/<int:pk>/play/",SongCreate.as_view()),

]