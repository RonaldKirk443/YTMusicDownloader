import pytubeModule
import eel


def init_eel():
    eel.init('web')
    eel.start('index.html', app_mode=True, mode="chrome")


config = open("config.txt")
my_dir = config.read()
url = "https://www.youtube.com/playlist?list=PLEbkAgZt4BIOuFJhHC-dV14IE2auWVeIU"

if url.find("playlist") != -1:
    titles = pytubeModule.get_titles(url)
    print(titles)
else:
    title = pytubeModule.get_title(url)
    print(title)

init_eel()


