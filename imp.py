import pygame
import config
import window
import spaceship


class GlobalFunctions:
    def __init__(self):
        pass

    def key_press(self):
        keys = pygame.key.get_pressed()
        pressed = []

        if keys[pygame.K_LEFT]:
            pressed.append('left')

        if keys[pygame.K_RIGHT]:
            pressed.append('right')

        if keys[pygame.K_UP]:
            pressed.append('up')

        if keys[pygame.K_DOWN]:
            pressed.append('down')

        if keys[pygame.K_SPACE]:
            pressed.append('space')

        return pressed















