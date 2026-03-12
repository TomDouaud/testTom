import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'badassradio.settings')
import django
django.setup()

from django.core.management import call_command
from django.contrib.auth.models import User
from blog.models import Playlist, Track, AlbumOfTheMonth, AlbumTrack
from django.core.files.uploadedfile import SimpleUploadedFile

def setup_data():
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin')

    if not Playlist.objects.exists():
        p = Playlist.objects.create(title='Test Playlist', playlist_type='basic', description='A test playlist')

        # Create dummy track
        audio_content = b"fake audio content"
        audio_file = SimpleUploadedFile("test.mp3", audio_content, content_type="audio/mpeg")
        Track.objects.create(playlist=p, title='Test Track 1', audio_file=audio_file)

    if not AlbumOfTheMonth.objects.exists():
        a = AlbumOfTheMonth.objects.create(title='Test Album', artist='Test Artist', description='A test album', month='2024-01-01')

        # Create dummy track
        audio_content = b"fake audio content"
        audio_file = SimpleUploadedFile("test2.mp3", audio_content, content_type="audio/mpeg")
        AlbumTrack.objects.create(album=a, title='Test Album Track 1', audio_file=audio_file)

if __name__ == '__main__':
    setup_data()
    print("Test data setup complete.")
