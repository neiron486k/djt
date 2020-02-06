from django.test import TestCase, Client
from django.contrib.auth.models import User
from rest_framework.test import APIClient
import json
from rest_framework.test import force_authenticate, APIRequestFactory


class PagesTestCase(TestCase):
    fixtures = ['pages.json']

    def setUp(self):
        self.user = User.objects.create(username="admin", password="admin", is_superuser=True, is_active=True,
                                        is_staff=True)
        self.client = Client()
        self.client.force_login(user=self.user)

    def test_get_pages(self):
        response = self.client.get('/api/v1/pages/')
        pages = response.data
        self.assertIn('count', pages)
        self.assertIn('results', pages)
        page = pages['results'][0]
        self.check_page_structure(page)

    def test_get_page(self):
        response = self.client.get('/api/v1/pages/1')
        self.check_page_structure(response.data)

    def test_patch_page(self):
        data = dict(title="updated title")
        response = self.client.patch('/api/v1/pages/1', data)
        print(response.data)

    def check_page_structure(self, page: dict):
        self.assertIn('id', page)
        self.assertIn('title', page)
        self.assertIn('description', page)
        self.assertIn('keywords', page)
        self.assertIn('content', page)
        self.assertIn('slug', page)
