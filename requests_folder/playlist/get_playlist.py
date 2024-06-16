import requests

from constants import USERNAME
from environment import token

def create_playlist(user_id, playlist_name, public=False, description=""):
    header = {'Authorization': token}
    body = {
        'name': playlist_name,
        'description': description,
        'public': public
    }
    response = requests.post(f'https://api.spotify.com/v1/users/{user_id}/playlists', json=body, headers=HEADER)
    assert create_playlist.status_code == 200
    return response.json()

def get_playlist(playlist,market=''):
    header = {'Authorization': token}
    response = requests.get(f'https://api.spotify.com/v1/albums/{playlist}?market={market}', headers=header)
    return response

def get_playlist_details(playlist_id):
    header = {'Authorization': token}
    response = requests.get(f'https://api.spotify.com/v1/playlists/{playlist_id}', headers=headers)
    return response.json()
