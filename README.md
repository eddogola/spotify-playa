# spotify-playa
a bot for downloading songs from personal spotify playlists

# Requirements
  * spotipy
  * pytube
  * youtube_dl
  * dotenv
  * youtubesearchpython

# Setting-up
You'll need to create an app(after logging in) at [Spotify developers dashboard](https://developers.spotify.com/dashboard/).
![create app screenshot](https://raw.githubusercontent.com/eddogola/spotify-playa/main/create-an-app-screenshot.png)

After creating an app, the app's auth keys(client id & client secret) will be generated. Copy these keys and replace the placeholders in the .env file with them.
![client auth keys screenshot](https://raw.githubusercontent.com/eddogola/spotify-playa/main/client-auth-keys-screenshot.png)

Click "EDIT SETTINGS" on the app's page. Add a redirect URI to the app. Replace the redirect URI placeholder in the .env file with the one you've added.
![app add redirect uri screenshot](https://raw.githubusercontent.com/eddogola/spotify-playa/main/redirect-uri-screenshot.png)

# Running it
Run the code. You'll be redirected to a page which will ask you to confirm the app's use with your account.This should happen only once, it won't pop when you run it other times.
That's it. You can tweak the code for it to download your spotify "liked songs," any other playlist, or even all playlists. I hope you enjoy it!
