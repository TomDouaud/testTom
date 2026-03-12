from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('reset-request/', views.password_reset_request, name='password_reset_request'),
    path('albums/', views.album_list, name='album_list'),
    path('playlists/<str:playlist_type>/', views.playlist_list, name='playlist_list'),
    path('playlist/<int:pk>/', views.playlist_detail, name='playlist_detail'),
]
