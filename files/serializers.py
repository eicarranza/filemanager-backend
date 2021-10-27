""" File serializers """

# Django REST Framework
from rest_framework import serializers

# Models
from files.models import (File, FileAllowed)

class FileSerializer(serializers.Serializer):
    id = serializers.IntegerField() 
    url = serializers.FileField()
    name = serializers.CharField()
    size = serializers.IntegerField()
    extension = serializers.CharField()
    created = serializers.DateTimeField()

class filesAllowedSerializer(serializers.Serializer):
    id = serializers.IntegerField() 
    name = serializers.CharField()
    extension = serializers.CharField() 
    is_active = serializers.BooleanField()


class fileSettingsSerializer(serializers.Serializer):
    id = serializers.IntegerField() 
    name = serializers.CharField()
    value = serializers.IntegerField()
    