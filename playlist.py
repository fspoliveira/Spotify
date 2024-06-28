import requests

def create_collaborative_playlist(user_id, playlist_name, access_token):
    url = f"https://api.spotify.com/v1/users/{user_id}/playlists"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    payload = {
        "name": playlist_name,
        "public": False,
        "collaborative": True,
        "description": "Playlist colaborativa criada via API"
    }

    response = requests.post(url, headers=headers, json=payload)
    response_data = response.json()
    return response_data['id']

def add_tracks_to_playlist(playlist_id, track_uris, access_token):
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    payload = {
        "uris": track_uris
    }

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code != 201:
        print("Erro ao adicionar faixas à playlist:", response.json())
        return False
    return True