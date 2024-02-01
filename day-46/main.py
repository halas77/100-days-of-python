from bs4 import BeautifulSoup
import requests







# CLIENT_ID = ""
# CLIENT_SECRET = ""
# TOKEN = ""


# user_time = input("Please choose a specific time: Valid Format[YYYY-MM-DD]: ")
# URL = "https://www.billboard.com/charts/hot-100/" + user_time

# response = requests.get(URL)
# data = response.text

# soup = BeautifulSoup(data, "html.parser")
# songs = soup.select("li ul li h3")

# formatted_songs = [song.getText().strip('\n\t') for song in songs]

# print(formatted_songs)


# import spotipy
# from spotipy.oauth2 import SpotifyOAuth

# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
#                                                client_secret=CLIENT_SECRET,
#                                                redirect_uri="http://localhost:8080",
#                                                scope="user-library-read"))

# results = sp.current_user_saved_tracks()
# for idx, item in enumerate(results['items']):
#     track = item['track']
#     print(idx, track['artists'][0]['name'], " – ", track['name'])











