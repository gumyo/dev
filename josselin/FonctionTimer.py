import pygame
from pygame.locals import *
pygame.init()

scoreRelativeTime, phyRelativeTime = 0, 0

def time(commandTimer, scoreRelativeTime, phyRelativeTime):
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
        return scoreRelativeTime, phyRelativeTime, dmin, min, dsec, sec
    elif commandTimer == 'phyTime':
        return scoreRelativeTime, phyRelativeTime, (pygame.time.get_ticks() + phyRelativeTime)
    return scoreRelativeTime, phyRelativeTime

while True:
    a = input('Commande :')
    b = time(a, scoreRelativeTime, phyRelativeTime)
    scoreRelativeTime, phyRelativeTime = b[0], b[1]
    if a == 'phyTime':
        print(b[2])
    elif a == 'scoreTime':
        print(b[2], '[dizaines de minutes]')
        print(b[3], '[minutes]')
        print(b[4], '[dizaines de secondes]')
        print(b[5], '[unités de secondes]')