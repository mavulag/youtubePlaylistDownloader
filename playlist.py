# Install yt-dlp via APT (more stable than Snap)

sudo apt update
sudo apt install yt-dlp

# Run this command to temporarily use it
~/.local/bin/yt-dlp --version

# A: Use full path every time
~/.local/bin/yt-dlp -o "%(playlist_index)s - %(title)s.%(ext)s" "https://www.youtube.com/playlist?list=<link>"

# B: Permanently fix your PATH (recommended)
Edit your shell config file:

nano ~/.bashrc

Or if you're using Zsh:

nano ~/.zshrc

Then add this line at the end:

export PATH="$HOME/.local/bin:$PATH"

Save and exit (Ctrl+O, Enter, then Ctrl+X), and reload the shell:

source ~/.bashrc

