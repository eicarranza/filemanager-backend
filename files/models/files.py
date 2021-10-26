""" Files model """

# Django
from django.db import models

# Utilities
from utils.models import FileManagerModel

class File(FileManagerModel):
    url = models.FileField(blank=False,  upload_to='media/files/', null=False)
    name = models.CharField(max_length=50, verbose_name='Name')
    size = models.PositiveSmallIntegerField()
    def __str__(self):
        return self.file.name