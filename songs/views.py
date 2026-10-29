from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions
from rest_framework.generics import ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView

from songs.serialiserz import SongSerializer
from songs.models import Songg

from movies.models import Movie

class SongCreate(APIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAdminUser]

    def post(self,request,pk=None):

        movie_id = pk

        movie_object = Movie.objects.get(id=movie_id)

        form_data = request.data

        serializer = SongSerializer(data=form_data)

        if serializer.is_valid():

            serializer.save(movie=movie_object,created_by=request.user)

            return Response(data=serializer.data)

        else:return Response(data=serializer.errors)

class SongListView(ListAPIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAdminUser]

    serializer_class = SongSerializer

    queryset = Songg.objects.all()        


class SongRetrieveUpdateDeleteView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    serializer_class = SongSerializer

    queryset = Songg.objects.all()




