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
        return (pygame.time.get_ticks() + scoreRelativeTime)
    elif commandTimer == 'phyTime':
        return (pygame.time.get_ticks() + phyRelativeTime)

while True:
    a = input('Commande [pause/play/reset/scoreReset/phyReset/scoreTime/phyTime] :')
    if a == 'phyTime' or a == 'scoreTime':
        print(time(a))
    else:
        time(a)