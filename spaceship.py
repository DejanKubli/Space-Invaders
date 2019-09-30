import imp


class SpaceShip(imp.GlobalFunctions):
    def __init__(self, x, y, w, h, v, win, img, proj_img):
        super().__init__()
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.v = v
        self.win = win
        self.projectiles = []
        self.img = img
        self.proj_img = proj_img

    def draw(self):
        self.win.blit(self.img, (self.x, self.y))
        for projectile in self.projectiles:
            projectile.draw()

    def move(self, directions):
        # get screen size
        screen_w, screen_h = imp.pygame.display.get_surface().get_size()

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

    def shoot(self, direction, new_shot):

        for proj in self.projectiles:
            proj.move(direction)
            if direction == 'up':
                if proj.y <= 0:
                    self.projectiles.remove(proj)

            if direction == 'down':
                if proj.y >= 800:
                    self.projectiles.remove(proj)

        if new_shot:
            if direction == 'up':
                self.projectiles.append(self.Projectile(x=self.x + self.w / 2 ,
                                                        y=self.y,
                                                        w=5, h=5, v=10,
                                                        win=self.win,
                                                        direction=direction,
                                                        img=self.proj_img))


            if direction == 'down':
                self.projectiles.append(self.Projectile(x=self.x + self.w / 2,
                                                        y=self.y + self.h,
                                                        w=5, h=5, v=10,
                                                        win=self.win,
                                                        direction=direction,
                                                        img=self.proj_img))

    class Projectile:
        def __init__(self, x, y, w, h, v, win, direction, img):
            self.x = x
            self.y = y
            self.w = w
            self.h = h
            self.dir = direction
            self.v = v
            self.win = win
            self.img = img

        def draw(self):
            self.win.blit(self.img, (self.x, self.y))

        def move(self, direction):
            if direction == 'left':
                self.x -= self.v

            if direction == 'right':
                self.x += self.v

            if direction == 'up':
                self.y -= self.v

            if direction == 'down':
                self.y += self.v





