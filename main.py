import window
import spaceship
import imp
# ************** CODE STARTS HERE ***************
# create window
win = window.Window(imp.config.WIN_SIZE, imp.config.TITLE)
# create players
player_1 = spaceship.SpaceShip(x=50, y=50, w=50, h=50, v=20,
                      win=win.win,
                      col=(205, 0, 0),
                      form='rectangle')
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
    player_1.shoot('up')


# main loop
imp.pygame.quit()
