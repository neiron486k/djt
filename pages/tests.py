from django.test import TestCase, Client
from .models import Pages
import json


class PagesTestCase(TestCase):
    def setUp(self):
        Pages.objects.create(slug="lion", content="roar")
        self.client = Client()

    def test_get_pages(self):
        response = self.client.get('/api/v1/pages/')
        pages = json.loads(response.content)
        self.assertIn('count', pages)
        self.assertIn('results', pages)
        page = pages['results'][0]
        self.assertIn('id', page)
        self.assertIn('title', page)
        self.assertIn('description', page)
        self.assertIn('keywords', page)
        self.assertIn('content', page)
        self.assertIn('slug', page)
