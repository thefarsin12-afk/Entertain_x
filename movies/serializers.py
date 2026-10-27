from django.contrib.auth.models import User

from rest_framework import serializers

from movies.models import Movie

from songs.models import Songg
from songs.serialiserz import SongSerializer


class SignUpSerilaizer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields = ["id","username","email","password"]


class MovieSerialiserz(serializers.ModelSerializer):

    song_count = serializers.SerializerMethodField(read_only=True)

    song = serializers.SerializerMethodField(read_only=True)

    class Meta:

        model = Movie

        fields = "__all__"

        read_only_fields = ["id","created_at","updated_at"] 

    def get_song_count(self,obj):

        return Songg.objects.filter(movie=obj).count()

    def get_song(self,obj):

        song_object = Songg.objects.filter(movie=obj)

        serializer_instance = SongSerializer(song_object,many=True)

        return serializer_instance.data

    

