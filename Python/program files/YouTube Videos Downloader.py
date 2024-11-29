from pytube import YouTube
import tkinter as tk
from tkinter import ttk
import threading
from datetime import datetime
import re

def sanitize_filename(filename):
    # Replace invalid characters with underscores
    return re.sub(r'[<>:"/\\|?*]', '_', filename)

class DownloadThread(threading.Thread):
    def __init__(self, url, quality, download_path):
        threading.Thread.__init__(self)
        self.url = url
        self.quality = quality
        self.download_path = download_path

    def run(self):
        try:
            yt = YouTube(self.url)
            video = yt.streams.filter(res=self.quality).first()

            if video is None:
                status_label.config(text="Selected quality not available", style="Info.TLabel")
                return

            status_label.config(text="Downloading...", style="Info.TLabel")

            current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            video_title = f"{yt.title}_{current_datetime}"
            sanitized_video_title = sanitize_filename(video_title)
            
            video.download(output_path=self.download_path,filename=f"{sanitized_video_title}.mp4")
            
            status_label.config(text="Download successful!", style="Success.TLabel")

        except Exception as e:
            status_label.config(text=f"Error: {str(e)}", style="Error.TLabel")

        finally:
            progress_bar.stop()  # Stop the progress bar

def download_video():
    video_url = url_entry.get()
    quality = quality_combo.get()
    
    progress_bar.start()  # Start the progress bar
    
    download_thread = DownloadThread(video_url, quality, r"C:\Users\kumar\Downloads")
    download_thread.start()

# Create the main window
root = tk.Tk()
root.title("YouTube Video Downloader")
root.geometry("500x300")
root.maxsize(650,400)
root.minsize(500,300)

# Styling
style = ttk.Style()
style.configure("Info.TLabel", foreground="blue")
style.configure("Success.TLabel", foreground="green")
style.configure("Error.TLabel", foreground="red")

# Create labels and entry fields
url_label = ttk.Label(root, text="Enter YouTube URL:")
url_label.pack(pady=10)
url_entry = ttk.Entry(root, width=40)
url_entry.pack(pady=5)

quality_label = ttk.Label(root, text="Select Quality:")
quality_label.pack(pady=10)
quality_combo = ttk.Combobox(root, values=["2160p","1440p","1080p", "720p", "480p", "360p", "240p", "144p"], state="readonly")
quality_combo.pack(pady=5)

download_button = ttk.Button(root, text="Download", command=download_video)
download_button.pack(pady=15)

status_label = ttk.Label(root, text="", font=("Arial", 12))
status_label.pack()

# Indeterminate progress bar
progress_bar = ttk.Progressbar(root, mode="indeterminate")
progress_bar.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
