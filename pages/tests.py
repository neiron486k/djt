from rest_framework.test import APITestCase
from mixer.backend.django import mixer
from django.contrib.auth import get_user_model


class PagesTestCase(APITestCase):
    def setUp(self):
        self.page = mixer.blend('pages.page')
        self.admin = mixer.blend(get_user_model(), is_superuser=True)

    def test_get_pages(self):
        mixer.cycle(5).blend('pages.page')
        response = self.client.get('/api/v1/pages/')
        self.assertEqual(200, response.status_code)
        pages = response.data
        self.assertIn('count', pages)
        self.assertIn('results', pages)
        page = pages['results'][0]
        self.check_page_structure(page)

    def test_get_page(self):
        response = self.client.get('/api/v1/pages/' + str(self.page.id))
        self.assertEqual(200, response.status_code)
        self.check_page_structure(response.data)

    def test_patch_page(self):
        title = "updated title"
        self.client.force_login(user=self.admin)
        response = self.client.patch('/api/v1/pages/' + str(self.page.id), dict(title=title))
        self.assertEqual(200, response.status_code)
        self.assertEqual(title, response.data['title'])

    def check_page_structure(self, page: dict):
        self.assertIn('id', page)
        self.assertIn('title', page)
        self.assertIn('description', page)
        self.assertIn('keywords', page)
        self.assertIn('content', page)
        self.assertIn('slug', page)
