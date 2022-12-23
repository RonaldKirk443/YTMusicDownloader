from pytube import Playlist

p = Playlist('https://www.youtube.com/playlist?list=PLEbkAgZt4BIOuFJhHC-dV14IE2auWVeIU')
config = open("config.txt")
my_dir = config.read()

for vid in p.videos:
    vid.use_oauth = True
    vid.allow_oauth_cache = True
    vid.streams.get_audio_only().download(output_path=my_dir, filename=vid.title + ".mp4", skip_existing=True)
    print(f"{vid.title} has downloaded!")