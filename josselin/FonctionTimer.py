import pygame
from pygame.locals import *
pygame.init()

scoreRelativeTime = 0
phyRelativeTime = 0

def time(commandTimer):
    global scoreRelativeTime
    global phyRelativeTime
    if commandTimer == 'pause':
        scoreRelativeTime += pygame.time.get_ticks()
        phyRelativeTime += pygame.time.get_ticks()
    elif commandTimer == 'play':
        scoreRelativeTime -= pygame.time.get_ticks()
        phyRelativeTime -= pygame.time.get_ticks()
    elif commandTimer == 'reset':
        scoreRelativeTime = 0 - pygame.time.get_ticks()
        phyRelativeTime = 0 - pygame.time.get_ticks()
    elif commandTimer == 'scoreReset':
        scoreRelativeTime = 0 - pygame.time.get_ticks()
    elif commandTimer == 'phyReset':
        phyRelativeTime = 0 - pygame.time.get_ticks()
    elif commandTimer == 'scoreTime':
<<<<<<< HEAD
        scoreTime, dmin, min, dsec, sec = (pygame.time.get_ticks() + scoreRelativeTime), 0, 0, 0, 0
        while scoreTime >= 600000:
            dmin += 1
            scoreTime -= 600000
        while scoreTime >= 60000:
            min += 1
            scoreTime -= 60000
        while scoreTime >= 10000:
            dsec += 1
            scoreTime -= 10000
        while scoreTime >=1000:
            sec += 1
            scoreTime -= 1000
        return dmin, min, dsec, sec
=======
        return (pygame.time.get_ticks() + scoreRelativeTime)
>>>>>>> 519364b498181b29bb8f2ab063677ec779975b90
    elif commandTimer == 'phyTime':
        return (pygame.time.get_ticks() + phyRelativeTime)

while True:
    a = input('Commande [pause/play/reset/scoreReset/phyReset/scoreTime/phyTime] :')
<<<<<<< HEAD
    b = time(a)
    if a == 'phyTime':
        print(b)
    elif a == 'scoreTime':
        print(b[0], '[dizaines de minutes]')
        print(b[1], '[minutes]')
        print(b[2], '[dizaines de secondes]')
        print(b[3], '[unités de secondes]')
=======
    if a == 'phyTime' or a == 'scoreTime':
        print(time(a))
    else:
        time(a)
>>>>>>> 519364b498181b29bb8f2ab063677ec779975b90
