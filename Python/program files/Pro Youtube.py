


from pytube import YouTube
from datetime import datetime
import os
import re
import tkinter as tk
from tkinter import messagebox, ttk

def sanitize_filename(filename):
    # Replace invalid characters with underscores
    return re.sub(r'[<>:"/\\|?*]', '_', filename)

def download_video():
    video_url = url_entry.get()

    try:
        # Create a YouTube object
        yt = YouTube(video_url)

        # Get the selected quality stream
        selected_quality = quality_combo.get()
        video_stream = yt.streams.get_by_resolution(selected_quality)

        if video_stream is None:
            messagebox.showerror("Error", "Selected quality not available.")
            return

        # Generate a title for the downloaded video with current date and time
        current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        video_title = f"{current_datetime}_{yt.title}"

        # Sanitize the video title to remove invalid characters
        sanitized_video_title = sanitize_filename(video_title)

        # Specify the directory where you want to save the downloaded video
        save_path = r"C:\Users\kumar\Downloads"

        # Combine the sanitized title with the save path
        full_path = os.path.join(save_path, sanitized_video_title + ".mp4")

        # Download the video with the sanitized title
        video_stream.download(output_path=save_path, filename=sanitized_video_title)
        messagebox.showinfo("Download Completed", "Video downloaded successfully!")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("YouTube Video Downloader")

# Create and place the URL entry field
url_label = tk.Label(root, text="Enter Video URL:")
url_label.pack()
url_entry = tk.Entry(root, width=50)
url_entry.pack()


# Available quality options (you can modify this based on your preferences)
quality_label = ttk.Label(root, text="Select Quality:")
quality_label.pack(pady=10)
quality_combo = ttk.Combobox(root, values=["1080p", "720p", "480p", "360p", "240p", "144p"], state="readonly")
quality_combo.pack(pady=5) # Set default value

# Create and place the Download button
download_button = tk.Button(root, text="Download", command=download_video)
download_button.pack()

# Start the main loop
root.mainloop()
