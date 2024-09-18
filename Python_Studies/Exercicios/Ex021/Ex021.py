import pygame

pygame.init()
pygame.mixer.init()

audio_file = "Exercicios/Ex021/Ex021.mp3"
pygame.mixer.music.load(audio_file)

pygame.mixer.music.play()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.mixer.music.stop()
            pygame.quit()
            exit()

pygame.event.wait()
