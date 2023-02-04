from PlaylistGenerator import PlaylistGenerator

# Dados de autenticação da API do SPOTIFY
CLIENT_ID = "014a404b53ad453fb300e85bccc47a37"
CLIENT_SECRET = "afbb22c6a4ff4bb3a59eccf76b903343"

print("Descubra quais eram as músicas mais tocatas\nBasta escolher a data.")
chosen_year = input("Insira aqui a data (YYYY-MM-DD): ")

playlist = PlaylistGenerator(chosen_year=chosen_year)
print(playlist.get_playlist())


# Year = 1994-10-28
