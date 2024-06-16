import pytest
from requests_folder.playlist.update_playlist import update_playlist

class TestUpdatePlaylist:
    def test_update_playlist(self):
        playlist_id = '1qISrmv0EN157fcAD0NOaE'
        new_name = 'Playlist Deea'
        new_description = 'This playlist has been updated using Spotify API'
        new_public_status = False

        update_response = update_playlist(playlist_id, new_name, new_description, new_public_status)

        assert update_response is not None, 'Failed to update playlist'
        assert update_response['name'] == new_name, 'Playlist name does not match'
        assert update_response['description'] == new_description, 'Playlist description does not match'
        assert update_response['public'] == new_public_status, 'Playlist visibility does not match'

    if __name__ == "__main__":
        pytest.main()
