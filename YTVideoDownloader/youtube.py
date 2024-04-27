from pytube import YouTube
# tkinter basic 2D GUI library
import tkinter as  tk
from tkinter import filedialog

def download_video(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download(output_path=save_path)

        print("Video downloaded successfully!")
    except Exception as e:
        print(e)

def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Seleced folder: {folder}")

    return folder


if __name__ == "__main__":
    root = tk.Tk() # allows tkinter to open file dialog
    root.withdraw() # hides the window
    video_url = input("Enter a YouTube url: ")
    save_dir = open_file_dialog()

    if not save_dir:
        print("Invalid save location.")
    else:
        download_video(video_url, save_dir)