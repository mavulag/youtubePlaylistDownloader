Python script to download a YouTube playlist using the pytube library. Before running the script, ensure you have installed the pytube library. You can install it using:

``` bash
pip install pytube
```

Python Script
``` bash
from pytube import Playlist

def download_youtube_playlist(playlist_url, download_path="."):
    try:
        playlist = Playlist(playlist_url)
        print(f"Downloading playlist: {playlist.title}")

        for video in playlist.videos:
            print(f"Downloading: {video.title}")
            video.streams.get_highest_resolution().download(output_path=download_path)
            print(f"Downloaded: {video.title}")

        print("All videos downloaded successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Provide the playlist URL and optional download path
    playlist_url = input("Enter the YouTube playlist URL: ")
    download_path = input("Enter the download path (default is current directory): ") or "."

    download_youtube_playlist(playlist_url, download_path)
```

How to Use:
Save the script in a file, e.g., download_playlist.py.
Run the script:
``` bash
python download_playlist.py
```
Input the YouTube playlist URL when prompted.

Specify the download path or press Enter to use the current directory.