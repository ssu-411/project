from django.test import TestCase
from django.contrib.auth.models import User


class AuthTest(TestCase):
    url = '/login/'

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        User.objects.create_user(username='username', password='password')

    def get_client_and_data(self):
        response = self.client.get(self.url)
        self.client = response.client
        data = {
            'csrftoken': response.cookies['csrftoken'].value,
            'username': 'username',
            'password': 'password',
        }
        return data

    def test_positive(self):
        data = self.get_client_and_data()
        response = self.client.post(self.url, data, follow=True)
        self.assertTrue(response.context['user'].is_authenticated)

    def test_invalid_password(self):
        data = self.get_client_and_data()
        data['password'] = 'invalid_password'
        response = self.client.post(self.url, data, follow=True)
        self.assertFalse(response.context['user'].is_authenticated)

    def test_invalid_username(self):
        data = self.get_client_and_data()
        data['username'] = 'invalid_username'
        response = self.client.post(self.url, data, follow=True)
        self.assertFalse(response.context['user'].is_authenticated)
