import window
import spaceship
import imp
import threading
from random import randint, choice

# ************** CODE STARTS HERE ***************
# create window
win = window.Window(imp.config.WIN_SIZE, imp.config.TITLE)


enemies = []
directions = ['left', 'right', 'up', 'down']


def create_enemy():
    threading.Timer(5.0, create_enemy).start()
    enemies.append(spaceship.SpaceShip(x=randint(0, imp.config.WIN_SIZE[0] - 50),
                                       y=randint(0, imp.config.WIN_SIZE[1] / 2),
                                       w=randint(20, 50),
                                       h=randint(20, 50),
                                       v=randint(3, 10),
                                       win=win.win,
                                       col=(205, 0, 0),
                                       form='rectangle'))


def move_enemy():
    threading.Timer(0.5, move_enemy).start()
    for enemy in enemies:
        enemy.move(choice(directions))
        enemy.shoot('down', True)


# create player
player_1 = spaceship.SpaceShip(x=200, y=200, w=50, h=50, v=20,
                      win=win.win,
                      col=(0, 205, 0),
                      form='rectangle')
create_enemy()
move_enemy()

run = True
# main loop
while run:
    imp.pygame.time.delay(100)

    for event in imp.pygame.event.get():
        if event.type == imp.pygame.QUIT:
            run = False

    # clear
    win.win.fill((0, 0, 0))

    player_1.move(player_1.key_press())
    player_1.shoot('up', 'space' in player_1.key_press())

    # check for all collisions
    for enemy in enemies:

        if imp.GlobalFunctions.collision('', player_1, enemy):
            enemies.remove(enemy)
        if imp.GlobalFunctions.collision('', enemy, player_1):
            print('GAME OVER!')
        enemy.draw()


# main loop
imp.pygame.quit()


