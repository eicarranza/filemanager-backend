""" Files views """

# Django REST Framework
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Models
from files.models import File

# Serializers
from files.serializers import FileSerializer

@api_view(['GET'])
def list_files(request):
    """ List files """
    files = File.objects.all()
    serializer = FileSerializer(files, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def upload_file(request):
    """Create file."""
    url = request.FILES['file']
    name = request.FILES['file'].name
    size = request.FILES['file'].size
    new_file = File.objects.create(url=url, name=name, size=size)
    
    data = {
        'name': new_file.name,
        'size': new_file.size,
        'created': new_file.created
    }

    return Response(data, status=status.HTTP_201_CREATED)