import requests

def get_album(token,album,market=''):
    header = {'Authorization': token}
    response = requests.get(f'https://api.spotify.com/v1/albums/{album}?market={market}', headers=header)
    return response

def get_album_without_market(token,id):
    header = {'Authorization': token}
    response = requests.get(f'https://api.spotify.com/v1/albums/{id}', headers=header)
    return response

def get_album_tracks(token,id):
    header = {'Authorization': token}
    response = requests.get(f'https://api.spotify.com/v1/albums/{id}/tracks', headers=header)
    return response.json()

def get_album_details(token,album_id):
    headers = {'Authorization': token}
    response = requests.get(f'https://api.spotify.com/v1/albums/{album_id}', headers=headers)
    return response.json()
