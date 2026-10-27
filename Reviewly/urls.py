from django.urls import path

from Reviewly.views import ReviewCreateView,ReviewListView,ReviewRetrieveUpdateDeleteView

urlpatterns = [

    path('movie/<int:pk>/add/',ReviewCreateView.as_view()),

    path('movie/all/',ReviewListView.as_view()),

    path('movie/all/<int:pk>/',ReviewRetrieveUpdateDeleteView.as_view()),
]