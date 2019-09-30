import pygame


class GlobalFunctions:
    def __init__(self):
        super().__init__()

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

    def collision(self, obj1, obj2):
        for proj in obj1.projectiles:
            if proj.x >= obj2.x - proj.w and proj.y >= obj2.y - proj.h \
                    and proj.x < obj2.x + obj2.w and proj.y < obj2.y + obj2.h:
                obj1.projectiles.remove(proj)
                return True







