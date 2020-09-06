from random import randint
import pgzrun

WIDHT = 500
HEIGT = 500
score = 0
game_over = False
play_time = 300

vos = Actor('hedgehog')
vos.pos = 100, 100

coin = Actor('coin')
coin.pos = 200, 200

def draw():
    screen.fill('black')
    vos.draw()
    coin.draw()
    screen.draw.text('score: ' + str(score), color='green', topleft=(10, 10))
    screen.draw.text('je hebt nog ' + str(play_time) + ' seconden', color='blue', topleft=(30, 30))

    if game_over:
        screen.fill('black')
        screen.draw.text('eindscore: ' + str(score), topleft=(10, 10), fontsize=60)



def draw_coin():
    coin.x = randint(50, (WIDHT - 20))
    coin.y = randint(50, (HEIGT - 20))
    pass

def tijd_om():
    global game_over
    global play_time
    play_time = play_time - 1
    print('!!!')
    screen.draw.text('je hebt nog ' + str(play_time) + ' seconden tot de einde van het spel!', color='blue', topleft=(30, 30))
    if play_time == 0:
        game_over = True
    else:
        clock.schedule(tijd_om, 1)


def update():
    global score

    if keyboard.left:
        vos.x = vos.x - 4
    elif keyboard.down:
        vos.y = vos.y + 4
    elif keyboard.up:
        vos.y = vos.y - 4
    elif keyboard.right:
        vos.x = vos.x + 4

        munt_verzameld = vos.colliderect(coin)

        if munt_verzameld:
            score = score + 10
            draw_coin()

clock.schedule(tijd_om, 1)
draw_coin()

pgzrun.go()