from pytube import Playlist

def get_youtube_playlist_videos(playlist_url):
    playlist = Playlist(playlist_url)
    videos = []
    
    for video in playlist.videos:
        title = video.title
        video_url = video.watch_url
        videos.append((title, video_url))
    
    return videos

if __name__ == "__main__":
    playlist_url = input("Enter the YouTube playlist URL: ")
    videos = get_youtube_playlist_videos(playlist_url)
    
    for title, url in videos:
        print(f'{title}: {url}')
