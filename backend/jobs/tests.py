from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import JobDescription


class JobDescriptionApiTests(APITestCase):
    def setUp(self):
        self.list_create_url = reverse('jobdescription-list-create')
        self.job_data = {
            'title': 'Software Engineer',
            'company': 'Acme Corp',
            'location': 'Remote',
            'description': 'Build great products.',
        }

    def test_create_job_description(self):
        response = self.client.post(self.list_create_url, self.job_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(JobDescription.objects.count(), 1)
        self.assertEqual(response.data['title'], self.job_data['title'])

    def test_get_job_description_list(self):
        JobDescription.objects.create(**self.job_data)
        response = self.client.get(self.list_create_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_job_description_detail(self):
        job = JobDescription.objects.create(**self.job_data)
        detail_url = reverse('jobdescription-detail', kwargs={'pk': job.id})
        response = self.client.get(detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['company'], self.job_data['company'])

    def test_update_job_description(self):
        job = JobDescription.objects.create(**self.job_data)
        detail_url = reverse('jobdescription-detail', kwargs={'pk': job.id})
        response = self.client.patch(detail_url, {'location': 'On-site'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['location'], 'On-site')

    def test_delete_job_description(self):
        job = JobDescription.objects.create(**self.job_data)
        detail_url = reverse('jobdescription-detail', kwargs={'pk': job.id})
        response = self.client.delete(detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(JobDescription.objects.count(), 0)
