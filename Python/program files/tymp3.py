
# from pytube import YouTube

# video_url=str(input("Enter Url: "))
# download_path = "F:/Music"

# yt = YouTube(video_url)
# video_stream = yt.streams.get_audio_only()

# video_stream.download(download_path)
# print("Download complete!")

import re

def sanitize_filename(filename):
    # Replace invalid characters with underscores
    return re.sub(r'[<>:"/\\|?*]', '_', filename)

a="y"

while a=="y":
    from pytube import YouTube

    video_url=str(input("Enter Url: "))
    download_path = "F:/Music"

    yt = YouTube(video_url)
    video_stream = yt.streams.get_audio_only()
    music_title=f"{yt.title}.mp3"
    sanitized_music_title = sanitize_filename(music_title)

    video_stream.download(download_path,filename=sanitized_music_title)


    

    print("Download complete!")
    
    a=str(input("Enter y to continue: "))