import re

with open('templates/blog/base.html', 'r') as f:
    content = f.read()

# We need to replace the entire ul block inside #navbarCollapse
search_str = """                <ul class="navbar-nav mb-2 mb-md-0 d-flex align-items-center">
                    <li class="nav-item dropdown mx-3">
                        <a class="nav-link dropdown-toggle p-0" href="#" id="playlistsDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false" style="border: none; background: none;">
                            <img src="{% static 'img/Playlists.png' %}" alt="Playlists" class="nav-image-link" style="height: 35px;">
                        </a>
                        <ul class="dropdown-menu dropdown-menu-dark" aria-labelledby="playlistsDropdown" style="background-color: rgba(0,0,0,0.8);">
                            <li><a class="dropdown-item" href="{% url 'playlist_list' 'basic' %}">Classiques</a></li>
                            <li><a class="dropdown-item" href="{% url 'playlist_list' 'movie' %}">Musiques de Films</a></li>
                            <li><hr class="dropdown-divider"></li>
                            <li><a class="dropdown-item" href="{% url 'album_list' %}">Albums du Mois</a></li>
                        </ul>
                    </li>
                    <li class="nav-item mx-3">
                         <a class="nav-link p-0" href="{% url 'playlist_list' 'movie' %}" style="border: none; background: none;">
                            <img src="{% static 'img/BO.png' %}" alt="Bandes Originales" class="nav-image-link" style="height: 25px;">
                        </a>
                    </li>
                </ul>"""

replace_str = """                <ul class="navbar-nav mb-2 mb-md-0 d-flex align-items-center">
                    <li class="nav-item mx-3">
                        <a class="nav-link p-0" href="{% url 'playlist_list' 'playlist' %}" style="border: none; background: none;">
                            <img src="{% static 'img/Playlists.png' %}" alt="Playlists" class="nav-image-link" style="height: 35px;">
                        </a>
                    </li>
                    <li class="nav-item mx-3">
                         <a class="nav-link p-0" href="{% url 'playlist_list' 'bande_originale' %}" style="border: none; background: none;">
                            <img src="{% static 'img/BO.png' %}" alt="Bandes Originales" class="nav-image-link" style="height: 25px;">
                        </a>
                    </li>
                    <li class="nav-item mx-3">
                         <a class="nav-link p-0" href="{% url 'playlist_list' 'mixtape' %}" style="border: none; background: none;">
                            <span class="fs-4 text-warning">Surprises</span>
                        </a>
                    </li>
                    <li class="nav-item mx-3">
                         <a class="nav-link p-0" href="{% url 'album_list' %}" style="border: none; background: none;">
                            <span class="fs-4 text-warning">Albums du Mois</span>
                        </a>
                    </li>
                </ul>"""

content = content.replace(search_str, replace_str)

with open('templates/blog/base.html', 'w') as f:
    f.write(content)
