from django.test import TestCase
from django.urls import reverse
from blog.models import Playlist, AlbumOfTheMonth
from datetime import datetime
from django.contrib.auth.models import User

class BadassRadioTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testadmin', password='testpassword')
        self.album = AlbumOfTheMonth.objects.create(
            title="Test Album",
            artist="Test Artist",
            description="Test Description",
            month=datetime.now().date()
        )
        self.playlist = Playlist.objects.create(
            title="Test Playlist",
            playlist_type="playlist"
        )

    def test_login_required_for_playlist(self):
        response = self.client.get(reverse('playlist_list', kwargs={'playlist_type': 'playlist'}))
        self.assertRedirects(response, f"/login/?next=/playlists/playlist/")

    def test_playlist_view_authenticated(self):
        self.client.login(username='testadmin', password='testpassword')
        response = self.client.get(reverse('playlist_list', kwargs={'playlist_type': 'playlist'}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Album")
        self.assertContains(response, "Test Playlist")

    def test_static_vinyl_logo_in_playlist_list(self):
        self.client.login(username='testadmin', password='testpassword')
        response = self.client.get(reverse('playlist_list', kwargs={'playlist_type': 'playlist'}))
        self.assertContains(response, 'vinyl-month.png')
