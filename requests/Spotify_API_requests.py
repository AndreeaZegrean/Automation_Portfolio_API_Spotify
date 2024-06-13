

def post_generate_token(clientId, clientSecret):
    header = {'Authorization': token}
    body = {
        'clientId': clientId,
        'clientSecret': clientSecret
    }
    response = requests.post('https://accounts.spotify.com/api/token', headers=header, json=body)
    return response.json()['accessToken']


response = post_generate_token('302fa0c6c00c481caa7099ebfabe3969', 'f3be51a3772b4d5f9c1dc36bcf195f7a')
print(response)

'''
def get_album(Album):
    header = {'Authorization': token}
    body = {
        'album_type' : album,
        'artists' : name
    }
    response = requests.get(f'https://api.spotify.com/v1/albums/{Album}', json=body)
    return response
'''