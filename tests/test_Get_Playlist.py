from environment import token
from requests_folder.playlist.get_playlist import get_playlist, create_playlist, get_playlist_details
import pytest

class TestGetPlaylist:

    def test_create_playlist(self):
        user_id = ''
        playlist_name = 'Test Playlist'
        playlist_description = 'This is a test playlist created using Spotify API'
        created_playlist = create_playlist(user_id, playlist_name, public=True, description=playlist_description,
                                           headers=HEADER)

        assert created_playlist is not None, 'Failed to create playlist'
        assert created_playlist['name'] == playlist_name, 'Playlist name does not match'
        assert created_playlist['description'] == playlist_description, 'Playlist description does not match'
        assert created_playlist['public'] == True, 'Playlist visibility does not match'

    if __name__ == "__main__":
        pytest.main()

    def test_get_playlist(self):
        get_playlist_response = get_playlist('1qISrmv0EN157fcAD0NOaE')
        assert get_playlist_response.status_code == 200

    def test_get_playlist_check_name(self):
        response = get_playlist('1qISrmv0EN157fcAD0NOaE')
        assert response.json()['name'] == 'Deea Andreea'

    def test_number_of_items(self):
        playlist_id = '1qISrmv0EN157fcAD0NOaE'
        expected_number_of_items = 49

        playlist_details = get_playlist_details(playlist_id)
        actual_number_of_items = playlist_details['tracks']['total']

        assert actual_number_of_items == expected_number_of_items, f'Expected {expected_number_of_items}, but got {actual_number_of_items}'





