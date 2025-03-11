# The Song class should receive a name (string), a length (float), and a single (bool) upon initialization. It has one method:
#   - get_info()
#       o Returns the information of the song in this format: "{song_name} - {song_length}"
#       The Album class should receive a name (string) upon initialization and might receive one or more songs. It also has instance attributes: published (False by default) and songs (an empty list). It has four methods:
#   - add_song(song: Song)
#       o Adds the song to the album and returns "Song {song_name} has been added to the album {name}."
#       o If the song is single, returns "Cannot add {song_name}. It's a single"
#       o If the album is published, returns "Cannot add songs. Album is published."
#       o If the song is already added, return "Song is already in the album."
#   - remove_song(song_name: str)
#       o Removes the song with the given name and returns "Removed song {song_name} from album {album_name}."
#       o If the song is not in the album, return "Song is not in the album."
#       o If the album is published, returns "Cannot remove songs. Album is published."
#   - publish()
#       o Publishes the album (set to True) and returns "Album {name} has been published."
#       o If the album is published, returns "Album {name} is already published."
#   - details()
#       o Returns the information of the album, with the songs in it, in the format:
#           "Album {name}
#           == {first_song_info}
#           == {second_song_info}
#           …
#           == {n_song_info}"
# The Band class should receive a name (string) upon initialization. It also has an attribute albums (an empty list).
# The class has three methods:
#   - add_album(album: Album)
#       o Adds an album to the collection and returns "Band {band_name} has added their newest album {album_name}."
#       o If the album is already added, returns "Band {band_name} already has {album_name} in their library."
#   - remove_album(album_name: str)
#       o Removes the album from the collection and returns "Album {name} has been removed."
#       o If the album is published, return "Album has been published. It cannot be removed."
#       o If the album is not in the collection, return "Album {name} is not found."
#   - details()
#       o Returns the information of the band, with their albums, in this format:
#           "Band {name}
#           {album details}
#           ...
#           {album details}"

from project.song import Song
from project.album import Album
from project.band import Band

# test
song = Song("Running in the 90s", 3.45, False)
print(song.get_info())
album = Album("Initial D", song)
second_song = Song("Around the World", 2.34, False)
print(album.add_song(second_song))
print(album.details())
print(album.publish())
band = Band("Manuel")
print(band.add_album(album))
print(band.remove_album("Initial D"))
print(band.details())

# 100/100

# output
# Running in the 90s - 3.45
# Song Around the World has been added to the album Initial D.
# Album Initial D
# == Running in the 90s - 3.45
# == Around the World - 2.34
# Album Initial D has been published.
# Band Manuel has added their newest album Initial D.
# Album has been published. It cannot be removed.
# Band Manuel
# Album Initial D
# == Running in the 90s - 3.45
# == Around the World - 2.34

# from project.song import Song
# from project.album import Album
# from project.band import Band
#
# import unittest
#
#
# class SongTest(unittest.TestCase):
#     def test_song_init(self):
#         song = Song("A", 3.15, False)
#         message = song.get_info()
#         expected = "A - 3.15"
#         self.assertEqual(message, expected)
#
#     def test_album_init(self):
#         album = Album("The Sound of Perseverance")
#         message = album.details().strip()
#         expected = "Album The Sound of Perseverance"
#         self.assertEqual(message, expected)
#
#     def test_add_song_working(self):
#         album = Album("The Sound of Perseverance")
#         song = Song("Scavenger of Human Sorrow", 6.56, False)
#         message = album.add_song(song)
#         expected = "Song Scavenger of Human Sorrow has been added to the album The Sound of Perseverance."
#         self.assertEqual(message, expected)
#
#     def test_add_song_already_added(self):
#         album = Album("The Sound of Perseverance")
#         song = Song("Scavenger of Human Sorrow", 6.56, False)
#         album.add_song(song)
#         message = album.add_song(song)
#         expected = "Song is already in the album."
#         self.assertEqual(message, expected)
#
#     def test_add_song_single(self):
#         album = Album("The Sound of Perseverance")
#         song = Song("Scavenger of Human Sorrow", 6.56, True)
#         message = album.add_song(song)
#         expected = "Cannot add Scavenger of Human Sorrow. It's a single"
#         self.assertEqual(message, expected)
#
#     def test_add_song_published_album(self):
#         album = Album("The Sound of Perseverance")
#         song = Song("Scavenger of Human Sorrow", 6.56, False)
#         album.publish()
#         message = album.add_song(song)
#         expected = "Cannot add songs. Album is published."
#         self.assertEqual(message, expected)
#
#     def test_remove_song_working(self):
#         album = Album("The Sound of Perseverance")
#         song = Song("Scavenger of Human Sorrow", 6.56, False)
#         album.add_song(song)
#         message = album.remove_song("Scavenger of Human Sorrow")
#         expected = "Removed song Scavenger of Human Sorrow from album The Sound of Perseverance."
#         self.assertEqual(message, expected)
#
#     def test_remove_song_not_in_album(self):
#         album = Album("The Sound of Perseverance")
#         song = Song("Scavenger of Human Sorrow", 6.56, False)
#         message = album.remove_song("Scavenger of Human Sorrow")
#         expected = "Song is not in the album."
#         self.assertEqual(message, expected)
#
#     def test_remove_song_album_published(self):
#         album = Album("The Sound of Perseverance")
#         song = Song("Scavenger of Human Sorrow", 6.56, False)
#         album.add_song(song)
#         album.publish()
#         message = album.remove_song("Scavenger of Human Sorrow")
#         expected = "Cannot remove songs. Album is published."
#         self.assertEqual(message, expected)
#
#     def test_publish(self):
#         album = Album("The Sound of Perseverance")
#         message = album.publish()
#         expected = album.published
#         self.assertTrue(expected)
#
#     def test_publish_message(self):
#         album = Album("The Sound of Perseverance")
#         message = album.publish()
#         expected = "Album The Sound of Perseverance has been published."
#         self.assertEqual(message, expected)
#
#     def test_details(self):
#         album = Album("The Sound of Perseverance")
#         song = Song("Scavenger of Human Sorrow", 6.56, False)
#         album.add_song(song)
#         message = album.details().strip()
#         expected = "Album The Sound of Perseverance\n== Scavenger of Human Sorrow - 6.56"
#
#     def test_init(self):
#         band = Band("Death")
#         message = f"{band.name} - {len(band.albums)}"
#         expected = "Death - 0"
#         self.assertEqual(message, expected)
#
#     def test_add_album_working(self):
#         band = Band("Death")
#         album = Album("The Sound of Perseverance")
#         message = band.add_album(album)
#         expected = "Band Death has added their newest album The Sound of Perseverance."
#         self.assertEqual(message, expected)
#
#     def test_add_album_already_added(self):
#         band = Band("Death")
#         album = Album("The Sound of Perseverance")
#         band.add_album(album)
#         message = band.add_album(album)
#         expected = "Band Death already has The Sound of Perseverance in their library."
#         self.assertEqual(message, expected)
#
#     def test_remove_album_working(self):
#         band = Band("Death")
#         album = Album("The Sound of Perseverance")
#         band.add_album(album)
#         message = band.remove_album("The Sound of Perseverance")
#         expected = "Album The Sound of Perseverance has been removed."
#         self.assertEqual(message, expected)
#
#     def test_remove_album_not_found(self):
#         band = Band("Death")
#         album = Album("The Sound of Perseverance")
#         message = band.remove_album("The Sound of Perseverance")
#         expected = "Album The Sound of Perseverance is not found."
#         self.assertEqual(message, expected)
#
#     def test_remove_album_published(self):
#         band = Band("Death")
#         album = Album("The Sound of Perseverance")
#         album.publish()
#         band.add_album(album)
#         message = band.remove_album("The Sound of Perseverance")
#         expected = "Album has been published. It cannot be removed."
#         self.assertEqual(message, expected)
#
#     def test_details(self):
#         band = Band("Death")
#         message = band.details().strip()
#         expected = "Band Death"
#         self.assertEqual(message, expected)
#
#
# if __name__ == '__main__':
#     unittest.main()