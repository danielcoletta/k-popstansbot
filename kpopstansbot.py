from requests.models import HTTPError
from spotipy.exceptions import SpotifyException
import telebot
import os
import re
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
#import secret

API_KEY = "2139263734:AAFPS2uGit79Wr6HsmsR669Na7z8Vu6HKdA"
CLIENT_ID = os.environ.get('CLIENT_ID')
CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
REDIRECT_URI = "https://k-pop-stans-bot.herokuapp.com/callback/" 
PLAYLIST_ID = os.environ.get('PLAYLIST_ID')
USER_ID = os.environ.get('USER_ID')

response_type = "code"
scope = "playlist-modify-private"

bot = telebot.TeleBot(API_KEY)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(username=USER_ID, scope=scope, client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI))
auth_manager = SpotifyOAuth(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, scope=scope)
sp = spotipy.Spotify(auth_manager=auth_manager)

@bot.message_handler(commands=['playlist'])
def playlist(message):
    bot.reply_to(message, "https://open.spotify.com/playlist/1GTP7dHqs9mKNoyZGCb8kt?si=e2dc42eac26342d3")

def check_for_link(message):
    return "https://" and "track" in message.text

@bot.message_handler(func=check_for_link)
def send_link(message):
    url = re.search("(?P<url>https?://[^\s]+)", message.text).group("url")
    try:
        if "spotify" in url:
            uri= extract_uri(message.text)
            add_track(uri)
            bot.reply_to (message, "bet")
        else:
            bot.reply_to (message, "Get good, send a Spotify link")

    except (HTTPError):
        if HTTPError.code == 403 or HTTPError.code == 401:
            bot.reply_to (message, "There was an error with Spotify authentication, fuck you Spotify for not letting me use token-based authentication")

    except: 
        bot.reply_to (message, "There was an issue adding the track, send the right link you simp")

def extract_uri(url):
    start = url.find("track/") + len("track/")
    end = url.find("?")
    prefix = str("spotify:track:")   
    track = url[start:end]
    uri = [prefix + track]
    return uri

def add_track(uri):
    sp.user_playlist_add_tracks(user = USER_ID, playlist_id = PLAYLIST_ID, tracks = uri)

def main():
    bot.polling()

if __name__ == "__main__":
    main()
