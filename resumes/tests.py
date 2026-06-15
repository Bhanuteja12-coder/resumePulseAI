from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from accounts.models import User


class ResumeApiTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='resumeuser@example.com', password='ResumePass123!')
        self.upload_url = reverse('resume-upload')
        self.login_url = reverse('token_obtain_pair')

        response = self.client.post(self.login_url, {'email': self.user.email, 'password': 'ResumePass123!'}, format='json')
        self.access_token = response.data['access']

    def authenticate(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

    def test_resume_upload_requires_auth(self):
        file_data = SimpleUploadedFile('resume.pdf', b'PDF file content', content_type='application/pdf')
        response = self.client.post(self.upload_url, {'file': file_data}, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_resume_upload_accepts_pdf(self):
        self.authenticate()
        file_data = SimpleUploadedFile('resume.pdf', b'%PDF-1.4', content_type='application/pdf')
        response = self.client.post(self.upload_url, {'file': file_data}, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['user'], self.user.id)

    def test_resume_upload_rejects_invalid_extension(self):
        self.authenticate()
        bad_file = SimpleUploadedFile('resume.txt', b'text content', content_type='text/plain')
        response = self.client.post(self.upload_url, {'file': bad_file}, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('file', response.data)
