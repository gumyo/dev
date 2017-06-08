import pygame
from pygame.locals import *
import sys


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

def save(display, point_stack, point_pile, register, regI, delay, sound, memory, stack):
    save = open("save.txt", "w")
    save.write(str(display) + '\n')
    save.write(str(point_stack) + '\n')
    save.write(str(point_pile) + '\n')
    save.write(str(register)[0: -1] + '\n')
    save.write(str(regI) + '\n')
    save.write(str(delay) + '\n')
    save.write(str(sound) + '\n')
    save.write(str(memory) + '\n')
    save.write(str(stack) + '\n')
    save.close()


def creat_list(liste):
    print('liste', liste)
    new_list = list()
    position = 0
    while position < len(liste):
        stock = str()
        if 48 <= ord(liste[position]) <= 57:
            stock += liste[position]
            while 48 <= ord(liste[position + 1]) <= 57:
                stock += liste[position + 1]
                position += 1
            new_list.append(int(stock))
        position += 1
    print(new_list)
    sys.exit()
    return new_list

def creat_dict(dico):
    register, compteur = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0}, 0
    for i in range(len(dico) -1):
        if dico[i - 1] == ' ' and dico[i - 2] == ':' and dico[i + 1] == ',':
            register[compteur] = int(dico[i])
            compteur += 1
        elif dico[i - 1] == ' ' and dico[i - 2] == ':' and dico[i + 1] != ',':
            register[compteur] = int(dico[i] + dico[i + 1])
            compteur += 1
            i += 1
    return register


def load():
    load = open("save.txt", "r")
    fichier = load.readlines()
    #display = list(fichier[0])
    point_stack = int(fichier[1])
    point_pile = int(fichier[2])
    register = creat_dict(fichier[3])
    print(register)
    regI = int(fichier[4])
    delay = int(fichier[5])
    sound = int(fichier[6])
    memory = creat_list(fichier[7])
    sys.exit()
    stack = creat_list(fichier[8])

    print(memory)
    
    return display, point_stack, point_pile, register, regI, delay, sound, memory, stack