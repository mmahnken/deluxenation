from django.test import TestCase
# from drawings.models import Notebook


class HomepageViewTestCase(TestCase):
    def test_homepage(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)


