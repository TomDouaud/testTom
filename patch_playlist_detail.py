import re

with open('templates/blog/playlist_detail.html', 'r') as f:
    content = f.read()

content = content.replace(
    "{% if playlist.playlist_type == 'basic' %}",
    "{% if playlist.playlist_type == 'playlist' or playlist.playlist_type == 'mixtape' %}"
)

content = content.replace(
    "if (playlistType === 'basic') {",
    "if (playlistType === 'playlist' || playlistType === 'mixtape') {"
)

content = content.replace(
    "if (playlistType === 'basic' && canvas) {",
    "if ((playlistType === 'playlist' || playlistType === 'mixtape') && canvas) {"
)

content = content.replace(
    "playlist.playlist_type == 'movie'",
    "playlist.playlist_type == 'bande_originale'"
)

content = content.replace(
    "playlistType === 'movie'",
    "playlistType === 'bande_originale'"
)

with open('templates/blog/playlist_detail.html', 'w') as f:
    f.write(content)
