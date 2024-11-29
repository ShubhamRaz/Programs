
from pytube import YouTube

video_url=str(input("Enter Url: "))
download_path = "F:/videos"

yt = YouTube(video_url)
video_stream = yt.streams.get_highest_resolution()

video_stream.download(download_path)
print("Download complete!")
