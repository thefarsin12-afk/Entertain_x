from django.urls import path

from songs.views import SongCreate,SongRetrieveUpdateDeleteView,SongListView
urlpatterns = [

   path("song/<int:pk>/play/",SongCreate.as_view()),

   path('all/song/',SongListView.as_view()),

   path("song/<int:pk>/",SongRetrieveUpdateDeleteView.as_view()),

]