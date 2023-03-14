# YouTube Playlist Downloader
This is a Python script that allows you to download all the videos from a YouTube playlist using the YouTube Data API.

## Installation
Clone the repository:

git clone https://github.com/mavulag/youtubePlaylistDownloader.git

## Import the required dependencies:

* import subprocess

* from pytube import Playlist

which are already written in the python file.

## Usage
Create a folder that the downloaded videos will be saved in the root of the project.

Replace 

* downloadDir="./folder_name" with the name you want your folder to be with and 

* playlistLink="paste_here_url" with the "url" of the playlist you want to download.

You can find those within the python script file (youtubePlaylistDownloader.py).

### To download a playlist, run the following command:

* python youtubePlaylistdownloader.py

The downloaded videos will be saved in the downloads directory you created before in the root of the project.

## Contributing
If you want to contribute to this project, feel free to open a pull request. You can also open an issue if you encounter any bugs or have any feature requests.
