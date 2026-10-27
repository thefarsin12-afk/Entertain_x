from django.urls import path

from rest_framework.authtoken.views import ObtainAuthToken

from movies.views import MoviesCreateListView
from movies.views import SignUpView
from movies.views import MoviesRetrieveUpdateDeleteView


urlpatterns = [

    path('register/',SignUpView.as_view()),

    path('login/',ObtainAuthToken.as_view()),

    path('add/',MoviesCreateListView.as_view()),

    path('add/<int:pk>/',MoviesRetrieveUpdateDeleteView.as_view()),
]