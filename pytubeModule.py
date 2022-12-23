from pytube import Playlist


def filterIllegalChars(title: str) -> str:
    chars = ['#', '%', '\\', '/', ':', '*', '?', '"', '<', '>', '|']
    new_title = title

    for char in chars:
        new_title = new_title.replace(char, "-")

    return new_title


def downloadPlaylist(url: str, my_dir: str):
    p = Playlist(url)

    for vid in p.videos:
        vid.use_oauth = True
        vid.allow_oauth_cache = True
        title = filterIllegalChars(vid.title)
        vid.streams.get_audio_only().download(output_path=my_dir, filename=title + ".mp3", skip_existing=True)
        print(f"{vid.title} has downloaded!")


if __name__ == "__main__":
    config = open("config.txt")
    my_dir = config.read()
    plink = input("Playlist Link: ")
    downloadPlaylist(plink, my_dir)
