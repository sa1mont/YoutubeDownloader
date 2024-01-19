from pytube import *
import os

video_url = "https://www.youtube.com/watch?v=VIDEO_ID"

yt = pytube.YouTube(video_url)

streams = yt.streams

video_stream = streams.filter(res="720p", file_extension="mp4").first()

video_stream.download()

print("Видео успешно загружено!")
