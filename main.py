import tkinter as tk
from ttkwidgets import CheckboxTreeview
from tkinter import ttk
import pytubeModule
import threading
import os


config = open("config.txt")
my_dir = config.read()
config.close()
global_title_list = []
# https://www.youtube.com/playlist?list=PLEbkAgZt4BIOuFJhHC-dV14IE2auWVeIU

window = tk.Tk()
window.title('PyTube Music Downloader')
window.minsize(0, 700)


def grab_titles():
    for root, directories, files in os.walk(my_dir):
        for filename in files:
            file_split = filename.split('.')
            file_split.pop(-1)
            file = "".join(file_split)
            global_title_list.append(file)


def grab_url():
    url_btn["state"] = tk.DISABLED
    download_btn["state"] = tk.DISABLED
    url = url_entry.get()
    print(f"'{url}'")

    if url.find("playlist") != -1:
        video_urls = pytubeModule.get_playlist_links(url)
        video_titles = pytubeModule.get_playlist_titles(url)
        video_thumbnails = pytubeModule.get_playlist_thumbnails(url)
        print(video_thumbnails)
    else:
        video_urls = [url]
        video_titles = [pytubeModule.get_title(url)]
        video_thumbnails = [pytubeModule.get_video_thumbnail(url)]
        print(video_thumbnails)

    for i in range(len(video_urls)):
        tree_table.insert(parent='', index='end', text="", tags="checked", values=(i+1, video_urls[i], video_titles[i], ""))

    url_btn["state"] = tk.ACTIVE
    download_btn["state"] = tk.ACTIVE
    status_lbl["text"] = "Playlist grabbed successfully"


def download_selected():
    url_btn["state"] = tk.DISABLED
    download_btn["state"] = tk.DISABLED
    checked_ids = tree_table.get_checked()
    total_id_count = len(checked_ids)

    for i in range(total_id_count):
        item_id = checked_ids[i]
        title = tree_table.item(item_id)["values"][2]

        if title not in global_title_list:
            status_lbl["text"] = f"Downloading {title}"
            url = tree_table.item(item_id)["values"][1]
            pytubeModule.download_video(url, my_dir)
            global_title_list.append(title)

        progress_bar['value'] = (i + 1) / total_id_count * 100
        tree_table.item(item_id, values=(tree_table.item(item_id)["values"][0],
                                         tree_table.item(item_id)["values"][1],
                                         tree_table.item(item_id)["values"][2],
                                         "Downloaded"))

    url_btn["state"] = tk.ACTIVE
    download_btn["state"] = tk.ACTIVE
    status_lbl["text"] = f"Download successful"


top_frame = tk.LabelFrame(master=window, height=300, borderwidth=5)
top_frame.grid(row=0, column=0)

url_label = tk.Label(master=top_frame, borderwidth=3, text="Enter playlist URL:")
url_label.grid(row=0, column=0, padx=3)

url_entry = tk.Entry(master=top_frame, borderwidth=3, width=80, bg="white", fg="black")
url_entry.insert(0, "https://www.youtube.com/playlist?list=PLEbkAgZt4BIOuFJhHC-dV14IE2auWVeIU")
url_entry.grid(row=0, column=1, padx=3)

url_btn = tk.Button(master=top_frame, borderwidth=3, width=10, text="Submit", command=lambda: threading.Thread(target=grab_url).start())
url_btn.grid(row=0, column=2, padx=3)


# Table Frame
table_frame = tk.Frame(master=window, height=700, borderwidth=10)
table_frame.grid(row=1, column=0)

tree_scroll = tk.Scrollbar(master=table_frame)
tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)

tree_table = CheckboxTreeview(master=table_frame, yscrollcommand=tree_scroll.set)
tree_table.pack()

tree_table['columns'] = ("ID", "URL", "Title", "Status")
tree_table.column("#0", width=50)
tree_table.column("ID", anchor=tk.CENTER, width=38)
tree_table.column("URL", width=0, stretch=tk.NO)
tree_table.column("Title", anchor="w", width=500)
tree_table.column("Status", anchor=tk.CENTER, width=100)

tree_table.heading("ID", text="ID", anchor=tk.CENTER)
tree_table.heading("Title", text="Title", anchor="w")
tree_table.heading("Status", text="Status", anchor=tk.CENTER)

tree_scroll.config(command=tree_table.yview)

# Bottom Download Frame
bottom_frame = tk.LabelFrame(master=window, height=100, borderwidth=5)
bottom_frame.grid(row=2, column=0)
bottom_frame.columnconfigure(1, minsize=553)

progress_bar = ttk.Progressbar(master=bottom_frame, orient='horizontal', mode='determinate', length=684)
progress_bar.grid(row=0, column=0, columnspan=3, padx=3)
progress_bar['mode'] = 'determinate'

status_text_lbl = tk.Label(master=bottom_frame, borderwidth=3, text="Status:", anchor="w")
status_text_lbl.grid(row=1, column=0, padx=3, sticky="w")

status_lbl = tk.Label(master=bottom_frame, borderwidth=3, text="Inactive", anchor="w")
status_lbl.grid(row=1, column=1, padx=3, sticky="ew")

download_btn = tk.Button(master=bottom_frame, borderwidth=3, width=10, text="Download", command=lambda: threading.Thread(target=download_selected).start())
download_btn.grid(row=1, column=2, padx=3, sticky="w")

grab_titles()
window.mainloop()