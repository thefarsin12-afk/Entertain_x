from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions
from rest_framework.generics import RetrieveAPIView,UpdateAPIView,DestroyAPIView

from movies.serializers import MovieSerialiserz
from movies.serializers import SignUpSerilaizer
from movies.models import Movie

class SignUpView(APIView):

    def post(self,request):

        form_data = request.data

        serialiserz = SignUpSerilaizer(data=form_data)

        if serialiserz.is_valid():

            cleaned_data = serialiserz.validated_data

            qs = User.objects.create_user(**cleaned_data)

            serialiserz = SignUpSerilaizer(qs)

            return Response(data=serialiserz.data)

        else:return Response(data=serialiserz.errors)


class MoviesCreateListView(APIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    def post(self,request):

        form_data = request.data

        serializer = MovieSerialiserz(data=form_data)

        if serializer.is_valid():

            serializer.save()

            return Response(data=serializer.data)

        else:return Response(data=serializer.errors)    

class MoviesRetrieveUpdateDeleteView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    serializer_class = MovieSerialiserz 

    queryset = Movie.objects.all()