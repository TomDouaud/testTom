import re

with open('templates/blog/home.html', 'r') as f:
    content = f.read()

content = content.replace(
    '<p class="mb-1">{{ playlist.get_playlist_type_display }}</p>',
    '<p class="mb-1">{{ playlist.get_playlist_type_display }}</p>'
)

with open('templates/blog/home.html', 'w') as f:
    f.write(content)
