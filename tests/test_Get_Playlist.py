from constante import USERNAME
from requests_folder.playlist.get_playlist import get_playlist, create_playlist

class TestGetPlaylist():

    def create_playlist(self):
        name = 'Updated playlist description'
        description = 'Playlist Deea'
        response = create_playlist(name, description)

        assert response.status_code == 201, 'Playlist was not created'
        assert response.json()['description'] == description or response.json()[
            'description'] is None, f'Expected description: {description}, Actual response: {response.json()['description']}'
        assert response.json()[
                   'name'] == name, f'Expected description: {name}, Actual response: {response.json()['name']}'
        assert response.json()['owner']['id'] == USERNAME, f'Expected {USERNAME}, Actual {response.json()['owner']['id']}'
    def test_get_playlist(self):
        get_playlist_response = get_playlist('1qISrmv0EN157fcAD0NOaE')
        assert get_playlist_response.status_code == 200

    def test_get_playlist_check_name(self):
        response = get_playlist('1qISrmv0EN157fcAD0NOaE')
        assert response.json()['name'] == 'Deea Amdreea'


