from rest_framework import serializers

class FileSerializer(serializers.Serializer):
    name = serializers.CharField()
    url = serializers.FileField()
    size = serializers.IntegerField()
    extension = serializers.CharField()


class CreateFileSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    url = serializers.FileField(required=False)
    size = serializers.IntegerField()
    extension = serializers.CharField(max_length=5)