from django.contrib.auth.models import User
from django.test import TestCase, Client
from registration.models import MyUser, genders


class RegisterTest(TestCase):
    url = '/register/'

    def get_client_and_data(self):
        response = self.client.get(self.url)
        self.client = Client(enforce_csrf_checks=True)
        data = {
            'csrftoken': response.cookies['csrftoken'].value,
            'username': 'RandomUsername',
            'password1': 'TopSecure100',
            'password2': 'TopSecure100',
            'age': 20,
            'gender': genders[0][0]
        }
        return response.client, data

    def test_positive(self):
        client, data = self.get_client_and_data()
        client.post(self.url, data)
        self.assertEqual(1, MyUser.objects.count())

    def test_password_mismatch(self):
        client, data = self.get_client_and_data()
        data['password2'] = 'Mismatching password'
        client.post(self.url, data)
        self.assertEqual(0, MyUser.objects.count())

    def test_incorrect_email(self):
        client, data = self.get_client_and_data()
        emails = ['login@domen', '(login)@domen.org', 'login@[domen].org', 'login@domen.{org}', 'login@do@men.org']
        for email in emails:
            data['email'] = email
            client.post(self.url, data)
        self.assertEqual(0, MyUser.objects.count())

    def test_incorrect_password(self):
        client, data = self.get_client_and_data()
        passwords = ['short', '12715845152545']
        for password in passwords:
            data['password1'] = password
            data['password2'] = password
            client.post(self.url, data)
        self.assertEqual(0, MyUser.objects.count())

    def test_incorrect_username(self):
        client, data = self.get_client_and_data()
        names = ['brackets()', 'brackets[]', 'brackets{}', 'slash/', 'slash\\', 'dollar$', 'and&', 'or|']
        for username in names:
            data['username'] = username
            client.post(self.url, data)
        self.assertEqual(0, MyUser.objects.count())

    def test_username_already_exists(self):
        client, data = self.get_client_and_data()
        User(username=data['username'], password=data['password1']).save()
        client.post(self.url, data)
        self.assertEqual(0, MyUser.objects.count())
