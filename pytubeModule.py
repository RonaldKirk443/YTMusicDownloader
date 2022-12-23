from pytube import Playlist

def downloadPlaylist(url: str, dir: str):
    p = Playlist(url)

    for vid in p.videos:
        vid.use_oauth = True
        vid.allow_oauth_cache = True
        vid.streams.get_audio_only().download(output_path=dir, filename=vid.title + ".mp3", skip_existing=True)
        print(f"{vid.title} has downloaded!")


if __name__ == "__main__":
    config = open("config.txt")
    my_dir = config.read()
    plink = input("Playlist Link: ")
    downloadPlaylist(plink, my_dir)
