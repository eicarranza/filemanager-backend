""" Files URLs """

# Django 
from django.urls import path

# Views
from files.views import list_files, upload_file, files_allowed, update_files_allowed

urlpatterns = [
    path('files/', list_files),
    path('files/upload', upload_file),
    path('files/files_allowed', files_allowed),
    path('files/files_allowed/<int:pk>', update_files_allowed),
]

# // python3 manage.py dumpdata <app_name>.<model_name>  > ./fixtures/<model_name>.json