import re

with open('templates/blog/playlist_list.html', 'r') as f:
    content = f.read()

search_str = """        {% if playlist_type == 'basic' %}
            Playlists Classiques
        {% else %}
            Musiques de Films
        {% endif %}"""

replace_str = """        {% if playlist_type == 'playlist' %}
            Playlists
        {% elif playlist_type == 'bande_originale' %}
            Bandes Originales
        {% elif playlist_type == 'mixtape' %}
            Surprises
        {% endif %}"""

content = content.replace(search_str, replace_str)

with open('templates/blog/playlist_list.html', 'w') as f:
    f.write(content)
