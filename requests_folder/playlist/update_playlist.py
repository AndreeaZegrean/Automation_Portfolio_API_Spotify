import requests
from environment import token

def update_playlist(album,market=''):
    header = {'Authorization': token}
    response = requests.put(f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks', headers=header)
    return response

