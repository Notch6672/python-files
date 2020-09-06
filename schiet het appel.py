import pgzrun
from random import randint
appel = Actor('apple')

def draw():
    screen.clear()
    appel.draw()

def plaats_appel():
    appel.x = randint(10, 800)
    appel.y = randint(10, 600)

def on_mouse_down(pos):
    if appel.collidepoint(pos):
        print('goed schot!')
        plaats_appel()
    else:
        print('je hebt gemist!')
        exit()

plaats_appel()

pgzrun.go()