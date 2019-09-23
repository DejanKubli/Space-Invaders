import pygame


def key_press():
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


class Window:
    def __init__(self, win_size, title):
        self.size = win_size
        self.title = title

        pygame.init()
        self.win = pygame.display.set_mode(self.size)
        pygame.display.set_caption(self.title)


class Player:
    # form = string of shape
    # col = color tuple RGB
    def __init__(self, x, y, w, h, v, win, col, form):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.v = v
        self.win = win
        self.col = col
        self.projectiles = []
        self.form = form

    def draw(self):
        if self.form == 'rectangle':
            pygame.draw.rect(self.win, self.col, (self.x, self.y, self.w, self.h))
            pygame.display.update()
        if self.form == 'triangle':
            pass

    def move(self, directions):
        # get screen size
        screen_w, screen_h = pygame.display.get_surface().get_size()

        # move left until you reach the edge of the screen
        if 'left' in directions:
            if self.x > 0 + self.w / 2:
                self.x -= self.v
        # move right until you reach the edge of the screen
        if 'right' in directions:
            if self.x < screen_w - self.w:
                self.x += self.v

        # move up until you reach the edge of the screen
        if 'up' in directions:
            if self.y > 0 + self.h / 2:
                self.y -= self.v

        # move down until you reach the edge of the screen
        if 'down' in directions:
            if self.y < screen_h - self.h:
                self.y += self.v

        self.draw()

    def shoot(self, direction):
        if 'space' in key_press():
            self.projectiles.append(Projectile(x=self.x + self.w / 2,
                                               y=self.y,
                                               w=5, h=5, v=10,
                                               win=self.win,
                                               direction=direction,
                                               col=(255, 0, 0)))
        for proj in self.projectiles:
            proj.move(direction)
            if direction == 'up':
                if proj.y <= 0:
                    self.projectiles.remove(proj)
            if direction == 'down':
                if proj.y >= 800:
                    self.projectiles.remove(proj)


class Projectile:
    def __init__(self, x, y, w, h, v, win, direction, col):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.dir = direction
        self.v = v
        self.win = win
        self.col = col

    def draw(self):
        pygame.draw.rect(self.win, self.col, (self.x, self.y, self.w, self.h))
        pygame.display.update()

    def move(self, direction):
        if direction == 'left':
            self.x -= self.v

        if direction == 'right':
            self.x += self.v

        if direction == 'up':
            self.y -= self.v

        if direction == 'down':
            self.y += self.v
        self.draw()











