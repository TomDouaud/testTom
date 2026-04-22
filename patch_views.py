import re

with open('blog/views.py', 'r') as f:
    content = f.read()

content = content.replace(
    "def playlist_list(request, playlist_type='basic'):",
    "def playlist_list(request, playlist_type='playlist'):"
)

content = content.replace(
    "movie_images = playlist.movie_images.all() if playlist.playlist_type == 'movie' else []",
    "movie_images = playlist.movie_images.all() if playlist.playlist_type == 'bande_originale' else []"
)

with open('blog/views.py', 'w') as f:
    f.write(content)
