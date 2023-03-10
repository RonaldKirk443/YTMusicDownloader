import pytube.exceptions
from pytube import Playlist, YouTube


def filter_illegal_chars(title: str) -> str:
    chars = ['#', '%', '\\', '/', ':', '*', '?', '"', '<', '>', '|']
    new_title = title

    for char in chars:
        new_title = new_title.replace(char, "-")

    return new_title


def download_playlist(url: str, my_dir: str):
    p = Playlist(url)

    for vid in p.videos:
        vid.use_oauth = True
        vid.allow_oauth_cache = True
        title = filter_illegal_chars(vid.title)
        vid.streams.get_audio_only().download(output_path=my_dir, filename=title + ".mp3", skip_existing=True)


def get_playlist_links(url: str) -> list[str]:
    p = Playlist(url)
    urls = []

    for url in p.url_generator():
        urls.append(url)

    return urls


def get_playlist_thumbnails(url: str) -> list[str]:
    p = Playlist(url)
    urls = []

    for vid in p.videos:
        urls.append(vid.thumbnail_url)

    return urls


def get_video_thumbnail(url: str) -> str:
    yt = YouTube(url)
    return yt.thumbnail_url


def get_playlist_titles(url: str) -> list[str]:
    p = Playlist(url)
    titles = []

    for vid in p.videos:
        titles.append(filter_illegal_chars(vid.title))

    return titles


def get_title(url: str) -> str:
    yt = YouTube(url)
    return filter_illegal_chars(yt.title)


def download_video(url: str, my_dir: str):
    vid = YouTube(url)
    title = filter_illegal_chars(vid.title)
    try:
        vid.streams.get_audio_only().download(output_path=my_dir, filename=title + ".mp3", skip_existing=True)
        return "Downloaded"
    except pytube.exceptions.AgeRestrictedError:
        return "Age Restricted"
    except pytube.exceptions.VideoPrivate:
        return "Private Video"
    except pytube.exceptions.VideoRegionBlocked:
        return "Region Block"
    except pytube.exceptions.VideoUnavailable:
        return "Video Unavailable"
    except:
        return "Download Error"



if __name__ == "__main__":
    config = open("config.txt")
    config_dir = config.read()
    plink = input("Playlist Link: ")
