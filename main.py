from pytube import *
import os

import pytube

# ������лка на видео YouTube
video_url = "https://www.youtube.com/watch?v=Sq6tf5xyr4o"

# С����даем объект YouTube
yt = pytube.YouTube(video_url)

# Получаем все доступные потоки видео
streams = yt.streams

# Фильтруем потоки по разрешению и формату
video_stream = streams.filter(res="720p", file_extension="mp4").first()

# Скачиваем видео
video_stream.download()

# Печатаем сообщение об успешной загрузке
print("Видео успешно загружено!")