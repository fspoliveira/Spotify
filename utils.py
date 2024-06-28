def read_urls(file_path):
    with open(file_path, 'r') as file:
        urls = file.readlines()

    track_uris = []
    for url in urls:
        url = url.strip()
        if 'open.spotify.com/track/' in url:
            track_id = url.split('track/')[1].split('?')[0]
            track_uris.append(f'spotify:track:{track_id}')
    return track_uris
