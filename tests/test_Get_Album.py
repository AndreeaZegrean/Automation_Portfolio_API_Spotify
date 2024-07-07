import unittest

from environment import get_token
from requests_folder.albums.get_album import get_album, get_album_without_market, get_album_details
from requests_folder.albums.get_album_tracks import get_album_tracks

class TestGetAlbum(unittest.TestCase):

    def setUp(self):
        self.token = get_token()

    def test_get_album(self):
        get_album_response = get_album(self.token,'1l1zcI8iwJg4WCb7jxHtbN')
        assert get_album_response.status_code == 200

    def test_get_album_does_not_exist(self):
        response = get_album_without_market(self.token,'1l1zcI8iwJg4WCb7jxHtbN00')
        assert response.status_code == 404

    def test_get_album_invalid(self):
        response = get_album_without_market(self.token,'6q6fbeSpRFPvhC4hPEfJQ9*')
        assert response.status_code == 400

    def test_get_album_tracks(self):
        response = get_album_tracks(self.token,'6q6fbeSpRFPvhC4hPEfJQ9*')
        assert response.status_code == 400

    def test_album_release_date(self):
        album_id = '71PfP4E9roOXAudea1aPGw'
        expected_release_date = '2024-03-08'

        album_details = get_album_details(album_id)
        actual_release_date = album_details['release_date']

        assert actual_release_date == expected_release_date, f'Expected {expected_release_date}, but got {actual_release_date}'

    def test_total_tracks(self):
        album_id = '71PfP4E9roOXAudea1aPGw'
        expected_total_tracks = 13

        album_details = get_album_details(self.token,album_id)
        actual_total_tracks = album_details['total_tracks']

        assert actual_total_tracks == expected_total_tracks, f'Expected {expected_total_tracks}, but got {actual_total_tracks}'

