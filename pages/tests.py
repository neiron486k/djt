from django.test import TestCase, Client
from .models import Page
import json


class PagesTestCase(TestCase):
    def setUp(self):
        self.page = Page.objects.create(slug="lion", content="some content here will be awesome")
        self.client = Client()

    def test_get_pages(self):
        response = self.client.get('/api/v1/pages/')
        pages = json.loads(response.content)
        self.assertIn('count', pages)
        self.assertIn('results', pages)
        page = pages['results'][0]
        self.check_page_structure(page)

    def test_get_page(self):
        response = self.client.get('/api/v1/pages/' + str(self.page.id))
        page = json.loads(response.content)
        self.check_page_structure(page)

    def check_page_structure(self, page: dict):
        self.assertIn('id', page)
        self.assertIn('title', page)
        self.assertIn('description', page)
        self.assertIn('keywords', page)
        self.assertIn('content', page)
        self.assertIn('slug', page)
