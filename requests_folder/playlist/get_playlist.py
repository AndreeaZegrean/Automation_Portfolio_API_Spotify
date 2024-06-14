import requests

from constante import USERNAME
from environment import token

def create_playlist(name, description):
    body = {
        'name': name,
        'description': description,
        'public': False
    }
    response = requests.post(f'https://api.spotify.com/v1/users/{USERNAME}/playlists', json=body, headers=HEADER)
    return response

def get_playlist(playlist,market=''):
    header = {'Authorization': token}
    response = requests.get(f'https://api.spotify.com/v1/albums/{playlist}?market={market}', headers=header)
    return response