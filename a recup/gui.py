import pygame
from pygame.locals import *



def run():
    while True:
        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN and event.key == K_RETURN:
            return True
        if event.type == pygame.KEYDOWN and event.key == K_F1:
            return False


def gui_register(register, screen):
    fontObj = pygame.font.Font('freesansbold.ttf', 15)
    screen.fill((0,0,0,255), (650, 20, 1920, 20))
    for i in range(16):
        texte = fontObj.render(str(hex(register[i])), True, (255, 255, 255, 255))
        screen.blit(texte, (650+40*i, 20))

def gui_memory(memory):
    mem = open("memory_map.txt", "w")
    mem.write(str(memory))
    mem.close()
    return False