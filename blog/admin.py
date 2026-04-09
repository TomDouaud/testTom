from django.contrib import admin
from .models import AlbumOfTheMonth, AlbumTrack, Playlist, Track, MovieImage, PasswordResetRequest, AtHomeImage

class AlbumTrackInline(admin.TabularInline):
    model = AlbumTrack
    extra = 1

class AtHomeImageInline(admin.TabularInline):
    model = AtHomeImage
    extra = 1

@admin.register(AlbumOfTheMonth)
class AlbumOfTheMonthAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'month', 'created_at')
    search_fields = ('title', 'artist')
    list_filter = ('month',)
    inlines = [AlbumTrackInline, AtHomeImageInline]

class TrackInline(admin.TabularInline):
    model = Track
    extra = 1

class MovieImageInline(admin.TabularInline):
    model = MovieImage
    extra = 1

@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('title', 'playlist_type', 'created_at')
    list_filter = ('playlist_type', 'created_at')
    search_fields = ('title',)
    inlines = [TrackInline, MovieImageInline]

@admin.register(PasswordResetRequest)
class PasswordResetRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'requested_at', 'is_resolved')
    list_filter = ('is_resolved', 'requested_at')
    search_fields = ('user__username',)
    actions = ['mark_resolved']

    def mark_resolved(self, request, queryset):
        queryset.update(is_resolved=True)
    mark_resolved.short_description = "Mark selected requests as resolved"
