import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'badassradio.settings')
django.setup()

from django.contrib.auth.models import User
from blog.models import AlbumOfTheMonth, Playlist

User.objects.create_superuser('admin', 'admin@example.com', 'admin')

# Create an album
AlbumOfTheMonth.objects.create(
    title='Test Album',
    artist='Test Artist',
    description='Test Desc',
    month='2024-05-01'
)

# Create playlists
Playlist.objects.create(title='Test Playlist', playlist_type='playlist')
Playlist.objects.create(title='Test BO', playlist_type='bande_originale')
Playlist.objects.create(title='Test Mixtape', playlist_type='mixtape')

print("Data created")
