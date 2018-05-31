import time

import pygame
from changeImage import setWallpaper


def go():
    filepath = "D:\\KwDownload\\song\\毛不易-盛夏.mp3"
    pygame.mixer.init()
    while True:
        track = pygame.mixer.music.load(filepath)
        pygame.mixer.music.play()
        time.sleep(5)
        pygame.mixer.music.stop()

def change(path):

    setWallpaper(path)


while True:

    for i in range(6):
        path="C:\\Users\\xiaolin\\Pictures\\Camera Roll\\00"+str(i)+".jpg"
        setWallpaper(path)
        time.sleep(1)
