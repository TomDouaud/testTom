import re

with open('blog/models.py', 'r') as f:
    content = f.read()

content = content.replace(
    "TYPE_CHOICES = (\n        ('basic', 'Basic Playlist'),\n        ('movie', 'Movie Soundtrack (Slideshow)'),\n    )",
    "TYPE_CHOICES = (\n        ('playlist', 'Playlist'),\n        ('bande_originale', 'Bande Originale'),\n        ('mixtape', 'Mixtape'),\n    )"
)

content = content.replace(
    "playlist_type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='basic')",
    "playlist_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='playlist')"
)

content = content.replace(
    "track_image = models.ImageField(upload_to='track_images/', blank=True, null=True, help_text=\"Image to display while playing this track (basic mode).\")",
    "track_image = models.ImageField(upload_to='track_images/', blank=True, null=True, help_text=\"Image to display while playing this track (playlist/mixtape mode).\")"
)

with open('blog/models.py', 'w') as f:
    f.write(content)
