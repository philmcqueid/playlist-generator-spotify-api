from PlaylistGenerator import PlaylistGenerator
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Dados de autenticação da API do SPOTIFY
CLIENT_ID = "014a404b53ad453fb300e85bccc47a37"
CLIENT_SECRET = "afbb22c6a4ff4bb3a59eccf76b903343"
REDIRECT_URI = "http://example.com"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

song_list = PlaylistGenerator(chosen_year=date)
song_names = song_list.get_playlist()

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
# Year = 1994-10-28


playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

# Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
