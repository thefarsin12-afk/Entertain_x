from rest_framework import serializers

from Reviewly.models import Review

class ReviewSerializer(serializers.ModelSerializer):

    movie = serializers.StringRelatedField(read_only=True)

    created_by = serializers.StringRelatedField(read_only = True)

    class Meta:

        model = Review

        fields = "__all__"

        read_only_fields = ["id","movie","created_by","created_at","update_at"]