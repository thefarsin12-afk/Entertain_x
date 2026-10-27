from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions

from songs.serialiserz import SongSerializer

from movies.models import Movie

class SongCreate(APIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    def post(self,request,pk=None):

        movie_id = pk

        movie_object = Movie.objects.get(id=movie_id)

        form_data = request.data

        serializer = SongSerializer(data=form_data)

        if serializer.is_valid():

            serializer.save(movie=movie_object,created_by=request.user)

            return Response(data=serializer.data)

        else:return Response(data=serializer.errors)




