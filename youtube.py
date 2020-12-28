import spotipy
import youtube_dl
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
from youtubesearchpython import VideosSearch

# load environment variables
load_dotenv(dotenv_path='youtube.env')

# API authenticates by reading credentials from environment variables
spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(scope='playlist-read-private'))

# open records file
file = open('tracks.txt', 'a+')

def get_all_playlists():
    return spotify.current_user_playlists()['items']

def get_daily_mixes_playlists():
    return [playlist for playlist in spotify.current_user_playlists()['items'] if playlist['description'].endswith('and more')]

def get_songs_from_playlist(playlist):
    return spotify.playlist_tracks(playlist['uri'])['items']

def get_liked_songs():
    total = spotify.current_user_saved_tracks()['total']
    liked_songs = list()
    limit = 50
    offset = 50
    while offset < total:
        liked_songs.extend(spotify.current_user_saved_tracks(limit=limit, offset=offset)['items'])
        offset += limit
    return liked_songs

def write_to_file(title):
    tracks = file.readlines()
    for track in tracks:
        if title+'\n' not in track:
            file.write("{}\n".format(title))

def song_youtube_search(title):
    try:
        result = VideosSearch(title, limit=1,).result()
        return result['result'][0]['link']
    except IndexError:
        pass

ydl_opts = {
    'format': 'bestaudio[ext=m4a]',
    'outtmpl': '~/Downloads/Music/%(title)s.%(ext)s',
}

def download_song(yt_link):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([yt_link])

def get_song_titles_from_songs(songs):
    for song in songs:
        artists = ''
        for artist in song['track']['artists']:
            if artists == '':
                artists += artist['name']
            else:
                artists += ', {}'.format(artist['name'])

        title = '{} , {}'.format(song['track']['name'], artists)
        try:
            download_song(song_youtube_search(title))
        except:
            pass
        write_to_file(title)

get_song_titles_from_songs(get_liked_songs())
#get_song_titles_from_songs(get_songs_from_playlist(get_daily_mixes_playlists()[3]))
#download_song(song_youtube_search("her hard place"))