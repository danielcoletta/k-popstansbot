import telebot
import os
import re
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import secret

API_KEY = secret.API_KEY
CLIENT_ID = secret.CLIENT_ID
CLIENT_SECRET =  secret.CLIENT_SECRET
REDIRECT_URI =  secret.REDIRECT_URI   
PLAYLIST_ID = secret.PLAYLIST_ID
USER_ID = secret.USER_ID

response_type = "code"
scope = "playlist-modify-private"

bot = telebot.TeleBot(API_KEY)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(username=USER_ID, scope=scope, client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI))

@bot.message_handler(commands=['playlist'])
def playlist(message):
    bot.reply_to(message, "https://open.spotify.com/playlist/1GTP7dHqs9mKNoyZGCb8kt?si=e2dc42eac26342d3")

def check_for_link(message):
    return "https://" and "track" in message.text

@bot.message_handler(func=check_for_link)
def send_link(message):
    url = re.search("(?P<url>https?://[^\s]+)", message.text).group("url")
    if "spotify" in url:
        bot.reply_to (message, "bet")
        uri = extract_uri(message.text)
        add_track(uri)
    
    else:
        bot.reply_to (message, "Please send a Spotify link")

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
