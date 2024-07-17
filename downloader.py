import customtkinter as ctk
from pytubefix import YouTube
from tkinter import filedialog

class Downloader:
    directory = "C:/"

    def __init__(self):
        super().__init__()

    def download_video(self, url):
        try:
            yt = YouTube(url)
            print(url)
        except:
            print("Invalid URL")
        
        mp4_streams = yt.streams.filter(progressive = True)
        return mp4_streams

    def select_directory(self, label):
        self.directory = filedialog.askdirectory()
        label.configure(text=self.directory)
        print(self.directory)

    