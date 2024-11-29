from pytube import YouTube
import tkinter as tk
from tkinter import ttk
from datetime import datetime

def download_video():
    video_url = url_entry.get()
    quality = quality_combo.get()

    try:
        yt = YouTube(video_url)
        video = yt.streams.filter(res=quality).first()
        
        download_path = r"C:\Users\kumar\Downloads"  # Specify your desired download path here
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        filename = f"{yt.title}_{timestamp}.mp4"
        
        status_label.config(text="Downloading...", style="Info.TLabel")
        video.download(output_path=download_path, filename=filename)
        status_label.config(text="Download successful!", style="Success.TLabel")

    except Exception as e:
        status_label.config(text=f"Error: {str(e)}", style="Error.TLabel")

# Create the main window
root = tk.Tk()
root.title("YouTube Video Downloader")

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
quality_combo = ttk.Combobox(root, values=["1080p", "720p", "480p", "360p", "240p", "144p"], state="readonly")
quality_combo.pack(pady=5)

download_button = ttk.Button(root, text="Download", command=download_video)
download_button.pack(pady=15)

status_label = ttk.Label(root, text="", font=("Arial", 12))
status_label.pack()

# Start the Tkinter event loop
root.mainloop()
