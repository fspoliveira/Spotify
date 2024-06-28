# Spotify Playlist Creator

Este é um programa em Python que permite a criação de uma playlist colaborativa no Spotify e a adição de faixas a ela, utilizando a API do Spotify.

## Funcionalidades

- Autoriza o aplicativo no Spotify.
- Cria uma playlist colaborativa no Spotify.
- Adiciona faixas à playlist criada.

## Requisitos

- Conta no Spotify.
- Aplicação registrada no [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications).
- Python 3.6 ou superior.
- Bibliotecas Python: `requests` e `python-dotenv`.

## Instalação

1. Clone este repositório:
    ```bash
    git clone https://github.com/seu_usuario/seu_repositorio.git
    cd seu_repositorio
    ```

2. Crie e ative um ambiente Conda:
    ```bash
    conda create -n spotify_playlist_creator python=3.9
    conda activate spotify_playlist_creator
    ```

3. Instale as dependências:
    ```bash
    pip install python-dotenv requests
    ```

4. Crie um arquivo `.env` na raiz do projeto e adicione suas credenciais do Spotify:
    ```env
    SPOTIFY_CLIENT_ID=seu_client_id
    SPOTIFY_CLIENT_SECRET=seu_client_secret
    SPOTIFY_REDIRECT_URI=http://localhost:8888/callback
    ```

### Arquivo `urls.txt`

Crie um arquivo `urls.txt` na raiz do projeto e adicione as URLs das faixas do Spotify que você deseja adicionar à playlist. As URLs devem estar no formato `https://open.spotify.com/track/{TRACK_ID}`.

## Uso

1. Execute o script principal:
    ```bash
    python main.py
    ```

2. Siga as instruções no prompt:
    - Visite a URL fornecida para autorizar o aplicativo no Spotify.
    - Cole a URL de redirecionamento após a autorização.
    - Insira o nome da sua playlist quando solicitado.

## Estrutura do Projeto

A estrutura de diretórios esperada é a seguinte:

 ```bash

 spotify_playlist_creator/
├── auth.py
├── user.py
├── playlist.py
├── utils.py
├── main.py
├── .env
├── urls.txt
└── README.md
  ```

## Contribuição

1. Faça um fork do projeto.
2. Crie uma branch para sua feature (`git checkout -b feature/fooBar`).
3. Commit suas mudanças (`git commit -am 'Add some fooBar'`).
4. Faça um push para a branch (`git push origin feature/fooBar`).
5. Crie um novo Pull Request.

## Licença

Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.
