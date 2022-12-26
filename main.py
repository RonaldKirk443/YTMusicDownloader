import tkinter as tk
import pytubeModule
import threading

config = open("config.txt")
my_dir = config.read()
# https://www.youtube.com/playlist?list=PLEbkAgZt4BIOuFJhHC-dV14IE2auWVeIU

window = tk.Tk()


def grab_url():
    url = url_entry.get()
    print(f"'{url}'")

    if url.find("playlist") != -1:
        video_urls = pytubeModule.get_links(url)
        video_titles = pytubeModule.get_titles(url)
    else:
        video_urls = [url]
        video_titles = [pytubeModule.get_title(url)]

    for i in range(len(video_urls)):
        confirmation_label["text"] = f"Downloading {video_titles[i]}"
        pytubeModule.download_video(video_urls[i], my_dir)

    confirmation_label["text"] = "Videos downloaded successfully"


top_frame = tk.Frame(master=window, height=500, borderwidth=3, bg="grey")
top_frame.pack(side=tk.TOP, expand=True)

url_label = tk.Label(master=top_frame, borderwidth=3, text="Enter playlist URL:")
url_label.grid(row=0, column=0, padx=3)

url_entry = tk.Entry(master=top_frame, borderwidth=3, width=80, bg="white", fg="black")
url_entry.grid(row=0, column=1, padx=3)

url_btn = tk.Button(master=top_frame, width=10, text="Submit", command=threading.Thread(target=grab_url).start)
url_btn.grid(row=0, column=2, padx=3)


mid_frame = tk.Frame(master=window, height=100, borderwidth=3)
mid_frame.pack(side=tk.BOTTOM ,expand=True)

confirmation_label = tk.Label(master=mid_frame, borderwidth=2, text="Downloading", relief=tk.SOLID)
confirmation_label.pack()

window.mainloop()