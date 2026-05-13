from django.test import TestCase
from blog.models import AlbumOfTheMonth
from datetime import date

class AlbumOfTheMonthTests(TestCase):
    def test_album_ordering(self):
        # Create albums in random order to test default ordering
        a1 = AlbumOfTheMonth.objects.create(
            title="Album A",
            artist="Artist 1",
            month=date(2023, 1, 1),
            description="desc"
        )
        a2 = AlbumOfTheMonth.objects.create(
            title="Album B",
            artist="Artist 2",
            month=date(2023, 2, 1),
            description="desc"
        )
        a3 = AlbumOfTheMonth.objects.create(
            title="Album Z",
            artist="Artist 3",
            month=date(2023, 2, 1),
            description="desc"
        )

        # Expected ordering: descending by month, then alphabetical by title
        # Month 2 (B, Z) then Month 1 (A)
        # So: Album B, Album Z, Album A

        albums = list(AlbumOfTheMonth.objects.all())
        self.assertEqual(albums[0].title, "Album B")
        self.assertEqual(albums[1].title, "Album Z")
        self.assertEqual(albums[2].title, "Album A")
