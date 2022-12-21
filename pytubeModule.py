from pytube import YouTube

yt = YouTube('https://youtu.be/GVAF07-2Xic')

counter = 0

for stream in yt.streams.filter(type="audio", ):
    type = stream.mime_type[6:]
    stream.download(filename=str(counter) + "." + type)
    print(stream)
    counter += 1