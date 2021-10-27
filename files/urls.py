""" Files URLs """

# Django 
from django.urls import path

# Views
from files.views import (list_files, upload_file, 
                            files_allowed, update_files_allowed, 
                            file_settings, update_file_settings)

urlpatterns = [
    path('files/', list_files),
    # path('files/filtered_files/<str:extension>', filtered_files),
    path('files/upload', upload_file),
    path('files/files_allowed', files_allowed),
    path('files/files_allowed/<int:pk>', update_files_allowed),
    path('files/file_settings', file_settings),
    path('files/file_settings/<int:pk>', update_file_settings),
]

# // python3 manage.py dumpdata <app_name>.<model_name>  > ./fixtures/<model_name>.json