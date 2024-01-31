from bs4 import BeautifulSoup
import requests

CLIENT_ID = "2a08c292e478430a8b418c76b50a06dc"
CLIENT_SECRET = "df161eb1ec2d4974a442eb967e067526"
TOKEN = "BQDBKJ5eo5jxbtpWjVOj7ryS84khybFpP_lTqzV7uV-T_m0cTfwvdn5BnBSKPxKgEb11"


# user_time = input("Please choose a specific time: Valid Format[YYYY-MM-DD]: ")
# URL = "https://www.billboard.com/charts/hot-100/" + user_time

# response = requests.get(URL)
# data = response.text

# soup = BeautifulSoup(data, "html.parser")
# songs = soup.select("li ul li h3")

# formatted_songs = [song.getText().strip('\n\t') for song in songs]

# print(formatted_songs)


import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri="http://localhost:8080",
                                               scope="user-library-read"))

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])








