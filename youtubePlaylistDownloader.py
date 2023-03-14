import subprocess
from pytube import Playlist

downloadDir="./folder_name"
playlistLink="paste_here_url"

playlist = Playlist(playlistLink)

for video in playlist.videos:
    video.streams.filter(type='video', progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(downloadDir)
