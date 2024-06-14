from requests_folder.albums.get_album import get_album, get_album_without_market
from requests_folder.albums.get_album_tracks import get_album_tracks


class TestGetAlbum():
    def test_get_album(self):
        get_album_response = get_album('1l1zcI8iwJg4WCb7jxHtbN')
        assert get_album_response.status_code == 200

    def test_get_album_does_not_exist(self):
        response = get_album_without_market('1l1zcI8iwJg4WCb7jxHtbN00')
        assert response.status_code == 404

    def test_get_album_invalid(self):
        response = get_album_without_market('6q6fbeSpRFPvhC4hPEfJQ9*')
        assert response.status_code == 400

    def test_get_album_tracks(self):
        response = get_album_tracks('6q6fbeSpRFPvhC4hPEfJQ9*')
        assert response.status_code == 400