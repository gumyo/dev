import pygame
from pygame.locals import *
from random import randint
import sys


def clear():  # 00E0
    display = []
    for i in range(32):
        display.append([0] * 64)
    return display  #check


def ret(point_stack, point_pile, stack):  # 00EE retourne à partir d'une sous fonction
    if point_stack > 0:
        point_stack -= 1
        point_pile = stack[point_stack]
    return point_stack, point_pile, stack  #check


def jump(opcode):  # 1NNN saute à l'adresse nnn
    val = (opcode & 0x0FFF) - 2
    point_pile = val
    return point_pile  #check


def call(opcode, point_pile, point_stack, stack):  # 2NNN Exec sous programme de nnn
    stack[point_stack] = point_pile
    if point_stack < 15:
        point_stack += 1
    point_pile = (opcode & 0x0FFF) - 2
    return point_pile, point_stack, stack #check


def next(opcode, register, point_pile):  # 3XNN si vx = nn on saut instruction suiv
    val = (opcode & 0x0F00) >> 8
    if register[val] == (opcode & 0x00FF):
        point_pile += 2
    return point_pile  #check


def nextNot(opcode, register, point_pile):  # 4XNN si vx != nn saut instruc suiv
    val = (opcode & 0x0F00) >> 8
    if register[val] != (opcode & 0x00FF):
        point_pile += 2
    return point_pile  #check


def nextReg(opcode, register, point_pile):  # 5XY0 si vx = vy saut instruc suiv
    vx = (opcode & 0x0F00) >> 8
    vy = (opcode & 0x00F0) >> 4
    if register[vx] == register[vy]:
        point_pile += 2
    return point_pile  #check


def setNnVx(opcode, register):  # 6XNN definit vx à nn
    vx = (opcode & 0x0F00) >> 8
    register[vx] = (opcode & 0x00FF)
    return register  #check


def addNnVx(opcode, register):  # 7XNN vx + nn
    vx = (opcode & 0x0F00) >> 8
    operation = register[vx] + (opcode & 0x00FF)
    register[0xF] = 0
    if operation > 0x00FF:
        operation &= 0x00FF
        register[0xF] = 1
    register[vx] = operation
    return register  #check


def setVxVy(opcode, register):  # 8XY0 definit vx à vy
    vx = (opcode & 0x0F00) >> 8
    vy = (opcode & 0x00F0) >> 4
    register[vx] = register[vy]
    return register  #check


def setVxOrVy(opcode, register):  # 8XY1 définit vx à vx "or" vy
    vx = (opcode & 0x0F00) >> 8
    vy = (opcode & 0x00F0) >> 4
    register[vx] |= register[vy]
    return register  #check


def setVxAndVy(opcode, register):  # 8XY2 définit vx à vx "and" vy
    vx = (opcode & 0x0F00) >> 8
    vy = (opcode & 0x00F0) >> 4
    register[vx] &= register[vy]
    return register  #check


def setVxXorVy(opcode, register):  # 8XY3 définit vx à vx "xor" vy
    vx = (opcode & 0x0F00) >> 8
    vy = (opcode & 0x00F0) >> 4
    register[vx] ^= register[vy]
    return register  #check


def addVyVx(opcode, register):  # 8XY4 additionne vy à vx, vf passe à 1 si dépassement memoire
    vx = (opcode & 0x0F00) >> 8
    vy = (opcode & 0x00F0) >> 4
    operation = register[vx] + register[vy]
    if operation > 0x00FF:
        operation &= 0x00FF
        register[0xF] = 1
    else:
        register[0xF] = 0
    register[vx] = operation
    return register  #check


def subVyVx(opcode, register):  # 8XY5 soustrait vy de vx, vf passe à 0 quand vx < 0
    vx = (opcode & 0x0F00) >> 8
    vy = (opcode & 0x00F0) >> 4
    operation = register[vx]
    if operation < register[vy]:
        operation = 0x00FF + operation - register[vy]
        register[0xF] = 0
    else:
        operation = register[vx] - register[vy]
        register[0xF] = 1
    register[vx] = operation
    return register  #check


def decVxRight(opcode, register):  # 8XY6 décale vx à droite de 1bit, init vf = bit poid faible vx
    vx = (opcode & 0x0F00) >> 8
    operation = bin(register[vx])[-1]
    register[0xF] = operation
    register[vx] = register[vx] >> 1
    return register  #check


def subVxVy(opcode, register):  # 8XY7 vx = vy - vx, vf passe à 0 quand vx < 0
    vx = (opcode & 0x0F00) >> 8
    vy = (opcode & 0x00F0) >> 4
    operation = register[vy]
    if operation < register[vx]:
        operation = 0x00FF + operation - register[vx]
        register[0xF] = 0
    else:
        operation = register[vy] - register[vx]
        register[0xF] = 1
    register[vx] = operation
    return register #check


def decVxLeft(opcode, register):  # 8XYE décale vx à gauche de 1bit, init vf = bit poid fort vx
    vx = (opcode & 0x0F00) >> 8
    val = bin(register[vx])[2]
    register[0xF] = val
    register[vx] = (register[vx] << 1) & 0x00FF
    return register  #check


def jmpIfVxNoVy(opcode, register, point_pile):  # 9XY0 saute l'instruction suiv si  vx != vy
    vx = (opcode & 0x0F00) >> 8
    vy = (opcode & 0x00F0) >> 4
    if register[vx] != register[vy]:
        point_pile += 2
    return point_pile  #check


def nnnI(opcode):  # ANNN affecte nnn à regI
    regI = opcode & 0x0FFF
    return regI #check


def nnnVo(opcode, register):  # BNNN pass à l'adresse nnn + v0
    point_pile = (opcode & 0x0FFF) + register[0] - 2
    return point_pile  #check


def rndVx(opcode, register):  # CXNN définit vx à un nombre aléatoire < 255 et > 0
    vx = (opcode & 0x0F00) >> 8
    register[vx] = randint(0, 255) & (opcode & 0x00FF)
    return register  #check


def drawDisplay(opcode, register, screen, display, memory, regI):  # DXYN
    Vx, Vy, N = register[(opcode & 0x0F00) >> 8], register[(opcode & 0x00F0) >> 4], opcode & 0x000F
    register[0xF] = 0
    tableauMemoire = []
    for i in range(N): tableauMemoire.append([0] * 8)
    noir, blanc = (0, 0, 0, 0), (255, 255, 255, 255)
    print(tableauMemoire)
    for i in range(N):
        for j in range(8):
            print("avant", bin(memory[regI + i]))
            try:
                tableauMemoire[i][j] = int(bin(memory[regI + i])[j + 2])
            except IndexError:
                tableauMemoire[i][j] = 0
            print("apres", tableauMemoire[i][j])
    print(tableauMemoire)
    for i in range(N):
        y = (Vy + i)
        if y > 31: break
        for j in range(8):
            x = (Vx + j)
            if x > 63: break

            if display[y][x] == 1 and tableauMemoire[i][j] == 1:
                register[0xF] = 1  # collision
                display[y][x] = 0
            elif (display[y][x] == 0 and tableauMemoire[i][j] == 1) or (
                            display[y][x] == 1 and tableauMemoire[i][j] == 1):
                display[y][x] = 1
            else:
                display[y][x] = 0

    for y in range(32):
        for x in range(64):
            couleur = noir if display[y][x] == 0 else blanc
            pygame.draw.rect(screen, couleur, (x * 10, y * 10, 10, 10))
    pygame.display.update()
    return display, register


def keyVxYes(opcode, register, keys, point_pile):  # EX9E si clé dans vx pressée instuction suivante
    vx = (opcode & 0x0F00) >> 8
    for event in pygame.event.get():
        if event.type == KEYDOWN or event.type == KEYUP:
            for i in range(16):
                if event.key == keys[i] and i == register[vx]:
                    point_pile += 2
                    return point_pile
    return point_pile  #check


def keyVxNo(opcode, register, keys, point_pile):  # EXA1 si clé dans vx non pressée instruc suivante
    vx = (opcode & 0x0F00) >> 8
    for event in pygame.event.get():
        if event.type == KEYDOWN or event.type == KEYUP:
            for i in range(16):
                if event.key != keys[i] and i != register[vx]:
                    point_pile += 2
                    return point_pile
    return point_pile  #check


def tmpVx(opcode, register, delay):  # FX07 définit vx à la valeur de la temporisation
    vx = (opcode & 0x0F00) >> 8
    register[vx] = delay & 0x00FF
    return register  #check


def key(opcode, register, keys):  # FX0A attend le signal d'une touche et la stock dans vx
    vx = (opcode & 0x0F00) >> 8
    while True:
        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            for i in range(16):
                if event.key == keys[i]:
                    register[vx] = i
                    return register  #check


def vxTmp(opcode, register):  # FX15 définit tempo à vx
    vx = (opcode & 0x0F00) >> 8
    delay = register[vx]
    return delay  #check


def soundVx(opcode, register):  # FX18 définit minuterie sonore à vx
    vx = (opcode & 0x0F00) >> 8
    sound = register[vx]
    return sound  #check


def addIVx(opcode, register, regI):  # FX1E ajoute regI au registe[vx], vf = 1 si dépassement
    vx = (opcode & 0x0F00) >> 8
    operation = regI + register[vx]
    if operation > 0xFFF:
        operation = operation & 0xFFF
        register[0xf] = 1
    else:
        register[0xf] = 0
    regI = operation
    return regI, register  #check


def IdgtVx(opcode, register):  # FX29 définit regI au caractère stocké dans vx
    vx = (opcode & 0x0F00) >> 8
    regI = (register[vx] * 5) & 0x0FFF
    return regI  #check


def stkVxI(opcode, register, regI, memory):  # FX33 stock le code decimal de vx dans I,I+1,I+2
    vx = (opcode & 0x0F00) >> 8
    memory[regI] = int(register[vx] // 100)
    memory[regI + 2] = int(register[vx] % 10)
    memory[regI + 1] = int((register[vx] / 10) % 10)
    return memory  #check


def stkVoVx(opcode, register, regI, memory):  # FX55 stock v0 à vx à partir de l'adresse regI
    vx = (opcode & 0x0F00) >> 8
    i = 0
    while i <= vx:
        memory[regI + i] = register[i]
        i += 1
    return memory  #check


def repVoVx(opcode, register, regI, memory):  # FX65 remplit v0 à vx avec val mem à partir de regI
    vx = (opcode & 0x0F00) >> 8
    i = 0
    while i <= vx:
        register[i] = memory[regI + i]
        i += 1
    return register  #check
