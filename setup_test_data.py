import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'badassradio.settings')
django.setup()

from django.contrib.auth.models import User
from blog.models import AlbumOfTheMonth, AlbumTrack, AlbumImage, Playlist, Track, MovieImage
from django.core.files.uploadedfile import SimpleUploadedFile
from datetime import date

def create_dummy_image(name, color='white'):
    from PIL import Image
    import io
    image = Image.new('RGB', (100, 100), color=color)
    img_io = io.BytesIO()
    image.save(img_io, format='JPEG')
    return SimpleUploadedFile(name, img_io.getvalue(), content_type='image/jpeg')

def run():
    print("Creating superuser...")
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin')
        print("Superuser created.")
    else:
        print("Superuser already exists.")

    print("Creating Album of the Month...")
    if not AlbumOfTheMonth.objects.exists():
        album = AlbumOfTheMonth.objects.create(
            title="Dummy Album",
            artist="The Dummies",
            description="A great dummy album.",
            month=date.today(),
            cover_image=create_dummy_image('album_cover.jpg')
        )
        AlbumTrack.objects.create(
            album=album,
            title="Track 1",
            audio_file=SimpleUploadedFile("dummy.mp3", b"dummy audio content")
        )
        AlbumImage.objects.create(
            album=album,
            image=create_dummy_image('at_home_1.jpg', 'red')
        )
        AlbumImage.objects.create(
            album=album,
            image=create_dummy_image('at_home_2.jpg', 'blue')
        )
        print("Album of the Month created.")

    print("Creating Basic Playlist...")
    if not Playlist.objects.filter(playlist_type='basic').exists():
        playlist = Playlist.objects.create(
            title="Dummy Playlist",
            playlist_type="basic",
            cover_image=create_dummy_image('playlist_cover.jpg')
        )
        Track.objects.create(
            playlist=playlist,
            title="Basic Track 1",
            audio_file=SimpleUploadedFile("dummy.mp3", b"dummy audio content"),
            track_image=create_dummy_image('track_cover.jpg', 'green')
        )
        print("Basic Playlist created.")

    print("Creating Movie Soundtrack...")
    if not Playlist.objects.filter(playlist_type='movie').exists():
        movie_playlist = Playlist.objects.create(
            title="Dummy Movie Soundtrack",
            playlist_type="movie",
            cover_image=create_dummy_image('movie_cover.jpg')
        )
        Track.objects.create(
            playlist=movie_playlist,
            title="Movie Track 1",
            audio_file=SimpleUploadedFile("dummy.mp3", b"dummy audio content")
        )
        MovieImage.objects.create(
            playlist=movie_playlist,
            image=create_dummy_image('movie_slide_1.jpg', 'yellow')
        )
        MovieImage.objects.create(
            playlist=movie_playlist,
            image=create_dummy_image('movie_slide_2.jpg', 'purple')
        )
        print("Movie Soundtrack created.")

    print("Creating Mixtape...")
    if not Playlist.objects.filter(playlist_type='mixtape').exists():
        mixtape = Playlist.objects.create(
            title="Dummy Mixtape",
            playlist_type="mixtape",
            cover_image=create_dummy_image('mixtape_cover.jpg', 'orange')
        )
        Track.objects.create(
            playlist=mixtape,
            title="Mixtape Track 1",
            audio_file=SimpleUploadedFile("dummy.mp3", b"dummy audio content")
        )
        print("Mixtape created.")

if __name__ == '__main__':
    run()
