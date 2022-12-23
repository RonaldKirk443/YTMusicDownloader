import pytubeModule

config = open("config.txt")
my_dir = config.read()
url = "https://www.youtube.com/playlist?list=PLEbkAgZt4BIOuFJhHC-dV14IE2auWVeIU"

if url.find("playlist") != -1:
    pytubeModule.downloadPlaylist(url, my_dir)
else:
    pytubeModule.downloadVideo(url, my_dir)

