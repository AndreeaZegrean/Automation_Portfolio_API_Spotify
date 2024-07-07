import requests

def create_playlist(token,user_id, playlist_name, public=False, description=""):
    header = {'Authorization': token}
    body = {
        'name': playlist_name,
        'description': description,
        'public': public
    }
    response = requests.post(f'https://api.spotify.com/v1/users/{user_id}/playlists', json=body, headers=header)
    return response.json()

def get_playlist(playlist,market=''):
    header = {'Authorization': token}
    response = requests.get(f'https://api.spotify.com/v1/albums/{playlist}?market={market}', headers=header)
    return response

def get_playlist_details(playlist_id):
    header = {'Authorization': token}
    response = requests.get(f'https://api.spotify.com/v1/playlists/{playlist_id}', headers=header)
    return response.json()
