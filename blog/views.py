from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import AlbumOfTheMonth, Playlist, Track, PasswordResetRequest
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse
import zipfile
import os

@login_required
def home(request):
    latest_album = AlbumOfTheMonth.objects.first()
    recent_playlists = Playlist.objects.all()[:5]
    return render(request, 'blog/home.html', {
        'latest_album': latest_album,
        'recent_playlists': recent_playlists,
    })

@login_required
def album_list(request):
    albums = AlbumOfTheMonth.objects.all()
    return render(request, 'blog/album_list.html', {'albums': albums})

@login_required
def album_detail(request, pk):
    album = get_object_or_404(AlbumOfTheMonth, pk=pk)
    tracks = album.tracks.all()
    past_albums = AlbumOfTheMonth.objects.exclude(pk=pk).order_by('-month')
    return render(request, 'blog/album_detail.html', {
        'album': album,
        'tracks': tracks,
        'past_albums': past_albums,
    })

@login_required
def download_album_zip(request, pk):
    album = get_object_or_404(AlbumOfTheMonth, pk=pk)
    tracks = album.tracks.all()

    response = HttpResponse(content_type='application/zip')
    response['Content-Disposition'] = f'attachment; filename="{album.title}.zip"'

    with zipfile.ZipFile(response, 'w') as zip_file:
        for track in tracks:
            if track.audio_file and os.path.exists(track.audio_file.path):
                zip_file.write(track.audio_file.path, os.path.basename(track.audio_file.path))

    return response

@login_required
def playlist_list(request, playlist_type='playlist'):
    playlists = Playlist.objects.filter(playlist_type=playlist_type)
    return render(request, 'blog/playlist_list.html', {
        'playlists': playlists,
        'playlist_type': playlist_type
    })

@login_required
def playlist_detail(request, pk):
    playlist = get_object_or_404(Playlist, pk=pk)
    tracks = playlist.tracks.all()
    movie_images = playlist.movie_images.all() if playlist.playlist_type in ['bande_originale', 'mixtapes'] else []

    return render(request, 'blog/playlist_detail.html', {
        'playlist': playlist,
        'tracks': tracks,
        'movie_images': movie_images,
    })

def password_reset_request(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        user = User.objects.filter(username=username).first()
        if user:
            PasswordResetRequest.objects.create(user=user)
            messages.success(request, 'Password reset request sent to admins.')
        else:
            messages.error(request, 'User not found.')
        return redirect('login')
    return render(request, 'blog/password_reset_request.html')
