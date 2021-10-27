""" Files model """

# Django
from django.db import models

# Utilities
from utils.models import FileManagerModel

class File(FileManagerModel):
    url = models.FileField(blank=False,  upload_to='storage/', null=False)
    name = models.CharField(max_length=50, verbose_name='Name')
    extension = models.CharField(max_length=10, verbose_name='extension')
    size = models.PositiveSmallIntegerField()
    def __str__(self):
        return self.name

class FileAllowed(FileManagerModel):
    name  = models.CharField(max_length=50, verbose_name='name')
    extension = models.CharField(max_length=5, verbose_name='Extension')
    is_active = models.BooleanField(default=True)
    
