from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions
from rest_framework.generics import ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView

from movies.models import Movie

from Reviewly.models import Review
from Reviewly.serilalizers import ReviewSerializer
from Reviewly.permission import IsOwner

class ReviewCreateView(APIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    def post(self,request,pk):

        movie_id = pk

        movie_object = Movie.objects.get(id=movie_id)

        form_data = request.data 

        serializer_instance = ReviewSerializer(data=form_data)

        if serializer_instance.is_valid():

            serializer_instance.save(movie=movie_object,created_by = request.user)

            return Response(data=serializer_instance.data)

        else:return Response(data=serializer_instance.errors)

class ReviewListView(ListAPIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    serializer_class = ReviewSerializer

    queryset = Review.objects.all()


class ReviewRetrieveUpdateDeleteView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [IsOwner]

    serializer_class = ReviewSerializer

    queryset = Review.objects.all()    