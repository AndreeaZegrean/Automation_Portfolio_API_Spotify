import unittest

class TestGetAlbum(unittest.TestCase):
    def test_get_album(self):
        submit_album_response = get_album('2019', 'VIDA')
        album = submit_album_response.json()['Album']
        response = get_an_album(album)
        self.assertEqual(response.status_code, 200)