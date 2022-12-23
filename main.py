import pytubeModule

config = open("config.txt")
my_dir = config.read()

while True:
    plink = input("Playlist Link (or n to exit): ")

    if plink == "n" or plink == "N":
        break

    if plink.find("playlist") != -1:
        titles = pytubeModule.download_playlist(plink, my_dir)
    else:
        title = pytubeModule.download_video(plink, my_dir)

    print("Videos downloaded successfully")
