""" Main URLs module. """

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('files.urls', 'files'), namespace='files')),
]
