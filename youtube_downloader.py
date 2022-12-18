# Copyright (C) December 2022 {Sunny Patel} <{sunnypatel124555@gmail.com}>

# This file is part of the {Youtube Downloader} project.

# The {Youtube Downloader} project can not be copied, distributed, and/or modified without the express
# permission of {Sunny Patel} <{sunnypatel124555@gmail.com}>.

import tkinter as tk
import requests
import re
from tkinter import filedialog

# create the main window
window = tk.Tk()
window.title("YouTube Downloader")
window.geometry("1280x720")
window.configure(bg="#000000")

# create a function to download the video
def download_video():
    # send a GET request to the YouTube video page
    response = requests.get(url_entry.get())

    # extract the video URL from the page source
    video_url = re.search(r'\"url\":\"(.+?)\"', response.text).group(1)

    # add the resolution and frame rate options to the video URL
    video_url += f"&range=bytes=0-&ratebypass=yes&adaptive_fmts=fps={fps_var.get()}&size={res_var.get()}"

    # download the video
    response = requests.get(video_url, stream=True)

    # save the video to a file
    file_path = filedialog.asksaveasfilename(defaultextension=".mp4")
    with open(file_path, "wb") as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)

    print("Video downloaded successfully!")

# create a function to display the thumbnail preview
def show_preview():
    # extract the video ID from the URL
    video_id = url_entry.get().split("v=")[1]

    # generate the thumbnail URL
    thumbnail_url = f"https://i.ytimg.com/vi/{video_id}/hqdefault.jpg"
    # create a frame to hold the URL input
frame = tk.Frame(window, bg="#000000")
frame.pack(side=tk.TOP)

# create a label for the URL input
label = tk.Label(frame, text="Enter a YouTube video URL:", font=("Arial", 18), fg="#FFFFFF", bg="#000000")
label.pack(side=tk.LEFT)

# create an entry field for the URL input
url_entry = tk.Entry(frame, font=("Arial", 18), fg="#FFFFFF", bg="#000000")
url_entry.pack(side=tk.LEFT)

# create a label for the resolution options
res_label = tk.Label(frame, text="Select a resolution:", font=("Arial", 18), fg="#FFFFFF", bg="#000000")
res_label.pack(side=tk.LEFT)

# create a dropdown menu for the resolution options
res_var = tk.StringVar(frame)
res_var.set("480p")
res_menu = tk.OptionMenu(frame, res_var, "480p", "720p", "1080p")
res_menu.config(font=("Arial", 18), bg="#000000", fg="#FFFFFF", activebackground="#000000", activeforeground="#FFFFFF")
res_menu.pack(side=tk.LEFT)

# create a label for the frame rate options
fps_label = tk.Label(frame, text="Select a frame rate:", font=("Arial", 18), fg="#FFFFFF", bg="#000000")
fps_label.pack(side=tk.LEFT)

# create a dropdown menu for the frame rate options
fps_var = tk.StringVar(frame)
fps_var.set("30fps")
fps_menu = tk.OptionMenu(frame, fps_var, "30fps", "60fps")
fps_menu.config(font=("Arial", 18), bg="#000000", fg="#FFFFFF", activebackground="#000000", activeforeground="#FFFFFF")
fps_menu.pack(side=tk.LEFT)

# create a button to show the thumbnail preview
preview_button = tk.Button(frame, text="Preview", font=("Arial", 18), fg="#FFFFFF", bg="#000000", command=show_preview)
preview_button.pack(side=tk.LEFT)

# create a canvas to hold the thumbnail preview
canvas = tk.Canvas(window, width=720, height=405, bg="#000000")
canvas.pack(side=tk.TOP)

# create a label to display the thumbnail preview
thumbnail_label = tk.Label(canvas, bg="#000000")
thumbnail_label.pack()

# create a button to download the video
download_button = tk.Button(window, text="Download", font=("Arial", 18), fg="#FFFFFF", bg="#00FF00", command=download_video)
download_button.pack(side=tk.BOTTOM, fill=tk.X, expand=True)

# run the main loop
window.mainloop()
