""" File serializers """

# Django REST Framework
from rest_framework import serializers

# Models
from files.models import File

class FileSerializer(serializers.Serializer):
    url = serializers.FileField()
    name = serializers.CharField()
    size = serializers.IntegerField()
    created = serializers.DateTimeField()