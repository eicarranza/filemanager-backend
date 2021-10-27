""" Main URLs module. """

from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('files.urls', 'files'), namespace='files')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
