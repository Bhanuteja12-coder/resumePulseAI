from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import User


class AuthApiTests(APITestCase):
    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('token_obtain_pair')
        self.refresh_url = reverse('token_refresh')
        self.verify_url = reverse('token_verify')
        self.me_url = reverse('user_me')

        self.credentials = {
            'email': 'tester@example.com',
            'first_name': 'Test',
            'last_name': 'User',
            'password': 'TestPass123!',
            'password2': 'TestPass123!',
        }

    def test_register_returns_user_and_tokens(self):
        response = self.client.post(self.register_url, self.credentials, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('user', response.data)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
        self.assertEqual(response.data['user']['email'], self.credentials['email'])
        self.assertTrue(User.objects.filter(email=self.credentials['email']).exists())

    def test_login_returns_tokens_and_user(self):
        User.objects.create_user(email=self.credentials['email'], password=self.credentials['password'])
        response = self.client.post(self.login_url, {'email': self.credentials['email'], 'password': self.credentials['password']}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
        self.assertIn('user', response.data)
        self.assertEqual(response.data['user']['email'], self.credentials['email'])

    def test_refresh_token_returns_new_access(self):
        user = User.objects.create_user(email=self.credentials['email'], password=self.credentials['password'])
        login_response = self.client.post(self.login_url, {'email': user.email, 'password': self.credentials['password']}, format='json')
        refresh_token = login_response.data['refresh']

        response = self.client.post(self.refresh_url, {'refresh': refresh_token}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)

    def test_verify_token_endpoint(self):
        user = User.objects.create_user(email=self.credentials['email'], password=self.credentials['password'])
        login_response = self.client.post(self.login_url, {'email': user.email, 'password': self.credentials['password']}, format='json')
        access_token = login_response.data['access']

        response = self.client.post(self.verify_url, {'token': access_token}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_me_endpoint_requires_auth_and_returns_user(self):
        user = User.objects.create_user(email=self.credentials['email'], password=self.credentials['password'])
        login_response = self.client.post(self.login_url, {'email': user.email, 'password': self.credentials['password']}, format='json')
        access_token = login_response.data['access']

        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        response = self.client.get(self.me_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], user.email)

    def test_me_endpoint_unauthenticated(self):
        response = self.client.get(self.me_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
