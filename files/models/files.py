""" Files model """

# Django
from django.db import models

# Utilities
from utils.models import FileManagerModel

class File(FileManagerModel):
    """ File model """
    name = models.CharField('Name', max_length=50)
    url = models.FileField('File', upload_to='media/files/', blank=True, null=True)
    size = models.PositiveSmallIntegerField()
    extension = models.CharField('Extension', max_length=5, default=0)

    def __str__(self):
        return self.name