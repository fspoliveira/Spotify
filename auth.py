import base64
import hashlib
import os
import requests
from urllib.parse import urlencode

# Função para gerar o code verifier
def generate_code_verifier():
    code_verifier = base64.urlsafe_b64encode(os.urandom(32)).rstrip(b'=').decode('utf-8')
    print(f"Generated code_verifier: {code_verifier}")  # Log para debug
    return code_verifier

# Função para gerar o code challenge a partir do code verifier
def generate_code_challenge(code_verifier):
    code_challenge_digest = hashlib.sha256(code_verifier.encode('utf-8')).digest()
    code_challenge = base64.urlsafe_b64encode(code_challenge_digest).rstrip(b'=').decode('utf-8')
    print(f"Generated code_challenge: {code_challenge}")  # Log para debug
    return code_challenge

# Função para obter a URL de autorização com PKCE
def get_auth_url(client_id, redirect_uri, code_challenge):
    params = {
        'client_id': client_id,
        'response_type': 'code',
        'redirect_uri': redirect_uri,
        'code_challenge_method': 'S256',
        'code_challenge': code_challenge,
        'scope': 'user-read-private user-read-email playlist-modify-public playlist-modify-private'
    }
    return f"https://accounts.spotify.com/authorize?{urlencode(params)}"

# Função para obter o token de acesso usando o código de autorização
def get_access_token(client_id, client_secret, redirect_uri, code, code_verifier):
    token_url = "https://accounts.spotify.com/api/token"
    payload = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': redirect_uri,
        'client_id': client_id,
        'client_secret': client_secret,
        'code_verifier': code_verifier
    }

    print(f"Payload for access token request: {payload}")  # Log para debug
    response = requests.post(token_url, data=payload)
    if response.status_code != 200:
        print("Erro ao obter o token de acesso:", response.json())
        return None

    response_data = response.json()
    return response_data.get('access_token')
