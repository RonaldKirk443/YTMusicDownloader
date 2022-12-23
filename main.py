import pytubeModule

config = open("config.txt")
my_dir = config.read()
url = "https://www.youtube.com/playlist?list=PLEbkAgZt4BIOuFJhHC-dV14IE2auWVeIU"

pytubeModule.downloadPlaylist(url, my_dir)
