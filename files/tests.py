import requests

# Django
from django.test import TestCase

# Models
from files.models import FileAllowed

class FileSuccessTestCase(TestCase):
    """ Files Allowed test case """
    
    def test_failed_file_allowed_creation(self):
        """ Random codes should be generate automatically """
        fileAllowed = FileAllowed.objects.create(
            name= 'JSON',
            extension= 'json',
            is_active= True
        )

    def test_get_files_check_status_code_equals_200(self):
        response = requests.get("http://localhost:8000/files/")
        assert response.status_code == 200

    def test_get_allowed_files_check_status_code_equals_200(self):
        response = requests.get("http://localhost:8000/files/files_allowed")
        assert response.status_code == 200

class FileFailedTestCase(TestCase):
    """ Files Allowed test case """
    
    def test_failed_file_allowed_creation(self):
        """ Random codes should be generate automatically """
        fileAllowed = FileAllowed.objects.create(
            name= 'JSON',
            extension= 'json',
            is_active= True
        )

    def test_get_files_check_status_code_equals_200(self):
        response = requests.get("http://localhost:8000/files/")
        assert response.status_code == 200

    def test_get_filtered_files_check_status_code_equals_200(self):
        response = requests.get("http://localhost:8000/files/filtered_files/")
        assert response.status_code == 200

    def test_put_file_settings_check_status_code_equals_200(self):
        response = requests.get("http://localhost:8000/files/file_settings/")
        assert response.status_code == 200