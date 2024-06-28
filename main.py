import os
from urllib.parse import urlparse, parse_qs
from dotenv import load_dotenv
from auth import get_auth_url, get_access_token, generate_code_verifier, generate_code_challenge
from user import get_user_id
from playlist import create_collaborative_playlist, add_tracks_to_playlist
from utils import read_urls

def main():
    load_dotenv()
    client_id = os.getenv('SPOTIFY_CLIENT_ID')
    client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')
    redirect_uri = os.getenv('SPOTIFY_REDIRECT_URI')

    code_verifier = generate_code_verifier()
    code_challenge = generate_code_challenge(code_verifier)

    print("Visite a seguinte URL para autorizar o aplicativo:")
    print(get_auth_url(client_id, redirect_uri, code_challenge))

    redirect_response = input("Cole a URL de redirecionamento aqui: ")
    parsed_url = urlparse(redirect_response)
    code = parse_qs(parsed_url.query).get('code')

    if not code:
        print("Erro: O código de autorização não foi encontrado na URL de redirecionamento.")
        exit()
    else:
        code = code[0]

    access_token = get_access_token(client_id, client_secret, redirect_uri, code, code_verifier)
    if not access_token:
        print("Erro: Não foi possível obter o token de acesso.")
        exit()
    
    print("Token de acesso obtido com sucesso!")

    user_id = get_user_id(access_token)
    print(f"Seu user ID do Spotify é: {user_id}")

    file_path = 'urls.txt'
    track_uris = read_urls(file_path)
    print(f"Track URIs: {track_uris}")  # Log para depuração

    playlist_name = input("Digite o nome da sua playlist: ")
    
    # Criação da playlist colaborativa
    playlist_id = create_collaborative_playlist(user_id, playlist_name, access_token)
    print(f"Playlist criada com ID: {playlist_id}")

    # Adicionando faixas à playlist
    success = add_tracks_to_playlist(playlist_id, track_uris, access_token)
    if success:
        print("Faixas adicionadas com sucesso à playlist!")
    else:
        print("Erro ao adicionar faixas à playlist.")

if __name__ == "__main__":
    main()
