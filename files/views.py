""" Files views """

# Django REST Framework
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Models
from files.models import (File, FileAllowed, FileSettings)

# Serializers
from files.serializers import (FileSerializer, 
                                filesAllowedSerializer, fileSettingsSerializer)

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
    new_file = File.objects.create(
            url=url, 
            name=name, 
            size=size, 
            extension=extension
            )
    
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


@api_view(['GET', 'PUT', 'DELETE'])
def update_files_allowed(request, pk):
    # find files by pk (id)
    try: 
        fileAllowed = FileAllowed.objects.get(pk=pk) 
        fileAllowed.is_active = request.data['is_active']
        
        fileAllowed.save()
        return Response({'message': 'File updated'}, status=status.HTTP_202_ACCEPTED)
    except FileAllowed.DoesNotExist: 
        return Response({'message': 'The file does not exist'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def file_settings(request):
    """ List file validations """
    fileSettings = FileSettings.objects.get()
    serializer = fileSettingsSerializer(fileSettings)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def update_file_settings(request, pk):
    # find files by pk (id)
    try: 
        fileSettings = FileSettings.objects.get(pk=pk) 
        fileSettings.value = request.data['value']
        fileSettings.save()
        return Response({'message': 'File updated'}, status=status.HTTP_202_ACCEPTED)
    except FileSettings.DoesNotExist: 
        return Response({'message': 'The file does not exist'}, status=status.HTTP_404_NOT_FOUND)