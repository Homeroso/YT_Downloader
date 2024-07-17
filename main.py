import customtkinter as tk
from downloader import Downloader
from tkinter import W, E, S, N

tk.set_appearance_mode("dark")
tk.set_default_color_theme("green")

Downloader = Downloader()

class Frame(tk.CTkFrame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master=master, **kwargs)
    
    def refresh(self):
        self.destroy()
        self.__init__()

class App(tk.CTk):
    resolutions = ["4320p", "2160p", "1440p", "1080p", "720p", "480p", "360p", "240p", "144p"]
    def __init__(self):
        super().__init__()
        

        #Title of the app
        self.title = tk.CTkLabel(master=self, text="YouTube Video Downloader", font=("Arial", 20))
        self.title.grid(row = 0, column = 0, columnspan = 2 ,pady=10)

        self.directory_frame = Frame(master=self)
        self.directory_frame.grid(row = 1, column = 0, columnspan = 2, pady=20, padx=60, sticky= E + W)

        self.download_frame = Frame(master=self)
        self.download_frame.grid(row = 2, column = 0, pady=20, padx=60)

        self.video_frame = Frame(master=self)
        self.video_frame.grid(row = 2, column = 1, pady=20, padx=60)

        #Current directory label
        self.directory_label = tk.CTkLabel(master=self.directory_frame, text=Downloader.directory, font=("Arial", 15))
        self.directory_label.pack(pady=10)

        #Change directory button
        self.directory_selection = tk.CTkButton(master=self.directory_frame, text="Select Directory", command= lambda: Downloader.select_directory(self.directory_label))
        self.directory_selection.pack(pady=10)

        #Entry for video URL
        self.url_entry = tk.CTkEntry(master=self.download_frame)
        self.url_entry.pack(pady=10, fill="x", expand=True)
        
        #Button to download video
        self.button = tk.CTkButton(master=self.download_frame, text="Download", command= lambda: self.options(Downloader.download_video(self.url_entry.get())))
        self.button.pack(pady=10)
    
    def options(self, options):
        res_options = []
        download_options = []
        for option in options:
            if option.resolution not in res_options and option.resolution != None:
                res_options.append(option.resolution)
                download_options.append(option)
        buttons = {}

        row = 0
        col = 0
        for option in download_options:
            def action(x = option.resolution):
                option.download(Downloader.directory)

            buttons[option.resolution] = tk.CTkButton(master=self.video_frame, text=option.resolution, command= action)
            buttons[option.resolution].grid(row = row, column = col, pady=10, padx=5)

            row+=1
            if row > 4:
                row = 0
                col += 1
        
        print(res_options)
        

app = App()
app.mainloop()