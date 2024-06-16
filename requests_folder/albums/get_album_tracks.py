import requests
from environment import token

def get_album_tracks(id):
    header = {'Authorization': token}
    response = requests.get(f'https://api.spotify.com/v1/albums/{id}/tracks', headers=header)
    return response.json()

