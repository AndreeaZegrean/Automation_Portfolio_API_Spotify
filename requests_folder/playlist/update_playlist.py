import requests
from environment import token

def update_playlist(playlist_id, new_name, new_description, new_public_status, header):
    header = {'Authorization': token}
    data = {
        'name': new_name,
        'description': new_description,
        'public': new_public_status
    }

    response = requests.put(f'https://api.spotify.com/v1/playlists/{playlist_id}', headers=headers, json=data)
    assert update_playlist.status_code == 200


