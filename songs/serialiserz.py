from rest_framework import serializers

from songs.models import Songg

class SongSerializer(serializers.ModelSerializer):

    class Meta:

        model = Songg

        fields = "__all__"

        read_only_fields = ["id","movie","track_number","created_by","created_at","updated_at"]

