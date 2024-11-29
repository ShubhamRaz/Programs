

from pytube import YouTube

# URL of the YouTube video you want to download
video_url = "https://youtu.be/2cdyfy8OjZ0"

# Create a YouTube object
yt = YouTube(video_url)

# Get the highest resolution stream available
video_stream = yt.streams.get_highest_resolution()

# Set the download path
download_path = r"C:\Users\kumar\OneDrive\Desktop"

# Download the video
video_stream.download(download_path)

print("Download complete!")
