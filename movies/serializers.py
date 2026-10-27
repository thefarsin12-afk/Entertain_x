from django.contrib.auth.models import User

from rest_framework import serializers

from movies.models import Movie

class SignUpSerilaizer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields = ["id","username","email","password"]


class MovieSerialiserz(serializers.ModelSerializer):

    class Meta:

        model = Movie

        fields = "__all__"

        read_only_fields = ["id","created_at","updated_at"] 