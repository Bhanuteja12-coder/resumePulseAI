import io

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

    def test_resume_upload_accepts_pdf_and_extracts_text(self):
        import fitz

        self.authenticate()
        pdf_buffer = fitz.open()
        page = pdf_buffer.new_page()
        page.insert_text((72, 72), 'Hello PDF Resume')
        file_data = SimpleUploadedFile('resume.pdf', pdf_buffer.write(), content_type='application/pdf')

        response = self.client.post(self.upload_url, {'file': file_data}, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['user'], self.user.id)
        self.assertIn('Hello PDF Resume', response.data['extracted_text'])

    def test_resume_upload_accepts_docx_and_extracts_text(self):
        from docx import Document

        self.authenticate()
        document = Document()
        document.add_paragraph('Hello DOCX Resume')
        buffer = io.BytesIO()
        document.save(buffer)
        buffer.seek(0)

        file_data = SimpleUploadedFile(
            'resume.docx',
            buffer.read(),
            content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        )

        response = self.client.post(self.upload_url, {'file': file_data}, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('Hello DOCX Resume', response.data['extracted_text'])

    def test_resume_upload_rejects_invalid_extension(self):
        self.authenticate()
        bad_file = SimpleUploadedFile('resume.txt', b'text content', content_type='text/plain')
        response = self.client.post(self.upload_url, {'file': bad_file}, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('file', response.data)

    def test_get_resume_list_returns_uploaded_resume(self):
        self.authenticate()
        document = self._create_docx_file('Hello DOCX Resume')
        upload_response = self.client.post(self.upload_url, {'file': document}, format='multipart')
        self.assertEqual(upload_response.status_code, status.HTTP_201_CREATED)

        response = self.client.get('/api/resumes/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertIn('Hello DOCX Resume', response.data[0]['extracted_text'])

    def test_get_resume_detail_returns_extracted_text(self):
        self.authenticate()
        document = self._create_docx_file('Hello DOCX Resume Detail')
        upload_response = self.client.post(self.upload_url, {'file': document}, format='multipart')
        self.assertEqual(upload_response.status_code, status.HTTP_201_CREATED)
        resume_id = upload_response.data['id']

        response = self.client.get(f'/api/resumes/{resume_id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('Hello DOCX Resume Detail', response.data['extracted_text'])

    def _create_docx_file(self, text):
        from docx import Document

        document = Document()
        document.add_paragraph(text)
        buffer = io.BytesIO()
        document.save(buffer)
        buffer.seek(0)
        return SimpleUploadedFile(
            'resume.docx',
            buffer.read(),
            content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        )
