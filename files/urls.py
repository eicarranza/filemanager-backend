""" Files URLs """

# Django 
from django.urls import path

# Views
from files.views import list_files, upload_file

urlpatterns = [
    path('files/', list_files),
    path('files/upload', upload_file),
]
