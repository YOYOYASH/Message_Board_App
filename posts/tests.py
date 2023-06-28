from django.test import TestCase
from django.urls import reverse

from .models import Post


class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(text='Just a test')

    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_object = f'{post.text}'
        self.assertEquals(expected_object, 'Just a test')


class HomePageViewTest(TestCase):
    def setUp(self):
        Post.objects.create(text='Just a test')

    def test_url_exists(self):
        resp = self.client.get('/')
        self.assertEquals(resp.status_code, 200)

    def test_view_url(self):
        resp = self.client.get(reverse('home'))
        self.assertEquals(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')
