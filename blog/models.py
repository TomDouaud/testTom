from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import FileExtensionValidator

class AlbumOfTheMonth(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    description = models.TextField()
    cover_image = models.ImageField(upload_to='albums/')
    month = models.DateField(help_text="The month this album represents (use the 1st of the month).")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-month']

    def __str__(self):
        return f"{self.title} - {self.artist} ({self.month.strftime('%B %Y')})"

class AlbumTrack(models.Model):
    album = models.ForeignKey(AlbumOfTheMonth, related_name='tracks', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    audio_file = models.FileField(
        upload_to='album_tracks/',
        help_text="Upload your audio file here.",
        validators=[FileExtensionValidator(allowed_extensions=['mp3', 'mp4', 'wav', 'ogg', 'm4a', 'aac', 'flac'])]
    )
    order = models.PositiveIntegerField(default=0, help_text="Will auto-increment if left at 0.")

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.order == 0:
            last_track = AlbumTrack.objects.filter(album=self.album).order_by('order').last()
            if last_track:
                self.order = last_track.order + 1
            else:
                self.order = 1
        super().save(*args, **kwargs)

class Playlist(models.Model):
    TYPE_CHOICES = (
        ('playlist', 'Playlist'),
        ('bande_originale', 'Bande Originale'),
        ('mixtape', 'Mixtape'),
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    playlist_type = models.CharField(max_length=15, choices=TYPE_CHOICES, default='playlist')
    cover_image = models.ImageField(upload_to='playlists/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class Track(models.Model):
    playlist = models.ForeignKey(Playlist, related_name='tracks', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    audio_file = models.FileField(
        upload_to='tracks/',
        validators=[FileExtensionValidator(allowed_extensions=['mp3', 'mp4', 'wav', 'ogg', 'm4a', 'aac', 'flac'])]
    )
    track_image = models.ImageField(upload_to='track_images/', blank=True, null=True, help_text="Image to display while playing this track (basic mode).")
    order = models.PositiveIntegerField(default=0, help_text="Will auto-increment if left at 0.")

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.order == 0:
            last_track = Track.objects.filter(playlist=self.playlist).order_by('order').last()
            if last_track:
                self.order = last_track.order + 1
            else:
                self.order = 1
        super().save(*args, **kwargs)

class MovieImage(models.Model):
    playlist = models.ForeignKey(Playlist, related_name='movie_images', on_delete=models.CASCADE, help_text="For Movie Soundtracks only.")
    image = models.ImageField(upload_to='movie_images/')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"Image {self.order} for {self.playlist.title}"

class AlbumImage(models.Model):
    album = models.ForeignKey(AlbumOfTheMonth, related_name='album_images', on_delete=models.CASCADE, help_text="For the 'at home' section.")
    image = models.ImageField(upload_to='album_home_images/')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

class PasswordResetRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    requested_at = models.DateTimeField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"Reset request for {self.user.username}"
