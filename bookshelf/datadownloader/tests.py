import os

from django.test import TestCase
from oauth2client.file import Storage

from bookshelf.settings import BASE_DIR


class DownloadTest(TestCase):
    COMMAND_DIR = os.path.join(BASE_DIR, 'datadownloader', 'management', 'commands')
    CREDENTIAL_DIR = os.path.join(COMMAND_DIR, '.credentials')
    CREDENTIAL_FILE = os.path.join(CREDENTIAL_DIR, 'secretfile.json')

    def test_credentials_exists(self):
        dir_ok = os.path.exists(self.CREDENTIAL_DIR) and os.path.isdir(self.CREDENTIAL_DIR)
        self.assertTrue(dir_ok)
        self.assertTrue(os.path.exists(self.CREDENTIAL_FILE))

    def test_credentials_correct(self):
        store = Storage(self.CREDENTIAL_FILE)
        credentials = store.get()
        self.assertFalse(credentials.access_token_expired)
