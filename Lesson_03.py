import pygame

print('Hello World!')

print('Este programa serve para abrir e reproduzir um áudio .mp3')

pygame.mixer.init()
pygame.mixer.music.load('test.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()