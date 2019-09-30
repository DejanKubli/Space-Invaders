import pygame
import config
import time
from imp import GlobalFunctions
from spaceship import SpaceShip
from random import randint
import os
pygame.init()



class Game:
    def __init__(self):
        self.enemies = []
        self.projectiles = []
        self.players = []
        self.timer = time.time()
        self.caption = pygame.display.set_caption(config.TITLE)
        self.win = pygame.display.set_mode(config.WIN_SIZE)
        self.bg = pygame.image.load(os.path.join('assets', 'bg.jpg'))
        self.bg = pygame.transform.scale(self.bg, config.WIN_SIZE)
        self.player_img = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'player.png')).convert_alpha(),
                                                 (75, 75))
        self.enemy_img = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'enemy_1.png')).convert_alpha(),
                                                (75, 75))
        self.proj_img = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'bullet.jpg')).convert_alpha(),
                                                (5, 10))

    def create_enemy(self):
        self.enemies.append(SpaceShip(x=randint(0, config.WIN_SIZE[0] - 50),
                                      y=randint(0, config.WIN_SIZE[1] / 2),
                                      w=randint(20, 50),
                                      h=randint(20, 50),
                                      v=randint(3, 10),
                                      win=self.win,
                                      img=self.enemy_img,
                                      proj_img=self.proj_img))

    def create_player(self):
        self.players.append(SpaceShip(x=10,
                                      y=10,
                                      w=10,
                                      h=10,
                                      v=10,
                                      win=self.win,
                                      img=self.player_img,
                                      proj_img=self.proj_img))

    def run(self):
        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(20)

            # main event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            # move all players
            for player in self.players:
                player.move(player.key_press())
                player.shoot('up', 'space' in player.key_press())

            # check for all collisions
            for enemy in self.enemies:
                instance = None
                if GlobalFunctions.collision(instance, self.players[0], enemy):
                    self.enemies.remove(enemy)
                if GlobalFunctions.collision(instance, enemy, self.players[0]):
                    print('GAME OVER!')

            self.draw()

    def draw(self):
        self.win.blit(self.bg, (0, 0))

        for enemy in self.enemies:
            enemy.draw()
        for player in self.players:
            player.draw()

        pygame.display.update()



game = Game()
game.create_player()
game.create_enemy()
game.run()

pygame.quit()
