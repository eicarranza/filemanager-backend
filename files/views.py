""" Files views """

# Django REST Framework
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Models
from files.models import File

# Serializers
from files.serializers import (FileSerializer, CreateFileSerializer)

@api_view(['GET'])
def list_files(request):
    """ List files """
    files = File.objects.all()
    serializer = FileSerializer(files, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def upload_file(request):
    serializer = CreateFileSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    data = serializer.data
    return Response(data)