""" Files admin """

# Django
from django.contrib import admin

# Model
from files.models import File

@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    """ File admin """

    list_display = (
        'url', 
    )