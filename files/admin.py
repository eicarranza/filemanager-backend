""" Files admin """

# Django
from django.contrib import admin

# Model
from files.models import (File, FileAllowed)

@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    """ File admin """

    list_display = (
        'name',
        'size',
        'extension',
        'url', 
    )


@admin.register(FileAllowed)
class FilesAllowedAdmin(admin.ModelAdmin):
    """ Files allowed admin """
    verbose_name_plural = 'Files Allowed'
    
    list_display = (
        'name', 
        'extension'
    )

    list_editable = ('extension',)