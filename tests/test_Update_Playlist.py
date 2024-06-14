from random import random

from requests_folder.playlist.get_playlist import get_playlist, create_playlist
from requests_folder.playlist.update_playlist import update_playlist


class TestUpdatePlaylist():
    def test_update_playlist(self):
        random_number = random.randint(0, 999999)
        name = f"New Playlist {random_number}'
        description = f'New Playlist description {random_number}'
        playlist_id = create_playlist(name, description).json()['id']

        updated_name = f'Updated Playlist {random_number}'
        updated_description = f'Updated playlist description {random_number}'
        response = update_playlist(playlist_id, updated_name, updated_description)

        assert response.status_code == 200, f'Update Playlist API did not work, Response status code: {response.status_code}'
        playlist = get_playlist(playlist_id).json()
        assert playlist['name'] == updated_name
        assert playlist['description'] == updated_description or playlist['description'] == ""
