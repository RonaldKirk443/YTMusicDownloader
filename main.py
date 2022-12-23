import pytubeModule

config = open("config.txt")
my_dir = config.read()
url = "https://www.youtube.com/playlist?list=PLEbkAgZt4BIOuFJhHC-dV14IE2auWVeIU"

if url.find("playlist") != -1:
    titles = pytubeModule.get_titles(url)
    print(titles)
else:
    title = pytubeModule.get_title(url)
    print(title)


