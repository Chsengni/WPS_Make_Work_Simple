import time

import pygame

filepath="D:\\KwDownload\\song\\毛不易-盛夏.mp3"
pygame.mixer.init()
track=pygame.mixer.music.load(filepath)
pygame.mixer.music.play()
time.sleep(5)
pygame.mixer.music.stop()
