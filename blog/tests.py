from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Playlist

class ViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test', password='password')
        self.client.login(username='test', password='password')
        self.playlist = Playlist.objects.create(title='Test Playlist', playlist_type='playlist')

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_playlist_list_view(self):
        response = self.client.get(reverse('playlist_list', args=['playlist']))
        self.assertEqual(response.status_code, 200)

    def test_playlist_detail_view(self):
        response = self.client.get(reverse('playlist_detail', args=[self.playlist.pk]))
        self.assertEqual(response.status_code, 200)
