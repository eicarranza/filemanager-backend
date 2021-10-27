""" Files views """

# Django REST Framework
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Models
from files.models import (File, FileAllowed)

# Serializers
from files.serializers import (FileSerializer, filesAllowedSerializer)

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
    
    extension = request.FILES['file'].name.split('.').pop()
    new_file = File.objects.create(url=url, name=name, size=size, extension=extension)
    
    data = {
        'name': new_file.name,
        'size': new_file.size,
        'extension': new_file.extension,
        'created': new_file.created
    }

    return Response(data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def files_allowed(request):
    """ List file validations """
    filesAllowed = FileAllowed.objects.all()
    serializer = filesAllowedSerializer(filesAllowed, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
def update_files_allowed(request):
    """Create file."""
    url = request.FILES['file']
    name = request.FILES['file'].name
    size = request.FILES['file'].size
    
    new_file = File.objects.create(url=url, name=name, size=size)
    
    data = {
        'name': new_file.name,
        'size': new_file.size,
        'extension': new_file.extension,
        'created': new_file.created
    }

    return Response(data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def update_files_allowed(request, pk):
    # find tutorial by pk (id)
    try: 
        fileAllowed = FileAllowed.objects.get(pk=pk) 
        fileAllowed.is_active = request.data['is_active']
        
        fileAllowed.save()
        return Response({'message': 'File updated'}, status=status.HTTP_202_ACCEPTED)
    except FileAllowed.DoesNotExist: 
        return Response({'message': 'The file does not exist'}, status=status.HTTP_404_NOT_FOUND)
 
    # GET / PUT / DELETE tutorial