import imp


class Window:
    def __init__(self, win_size, title):
        self.size = win_size
        self.title = title

        imp.pygame.init()
        self.win = imp.pygame.display.set_mode(self.size)
        imp.pygame.display.set_caption(self.title)
