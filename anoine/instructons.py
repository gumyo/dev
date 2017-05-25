import pygame
from pygame.locals import *
from random import randint
from config import


def ret(pointPile, pointStack, stack):			#00EE retourne à partir d'une sous fonction
	if pointStack > 0:
		pointStack -= 1
		pointPile = stack[pointStack]
		return pointStack, pointPile, stack

def jump(opcode, pointPile):					#1NNN saute à l'adresse nnn
	val = (opcode & 0x0FFF) - 2
	pointPile = val
	return pointPile

def call(opcode, pointPile, pointStack, stack):	#2NNN Exec sous programme de nnn
	stack[pointStack] = pointPile
	if pointStack < 15:
		pointStack += 1
	pointPile = (opcode & 0x0FFF) - 2
	return pointPile, pointStack, stack

def next(opcode, register, pointPile):			#3XNN si vx = nn on saut instruction suiv
	val = (opcode & 0x0F00) >> 8
	if register[val] == (opcode & 0x00FF):
		pointPile += 2
		return pointPile

def nextNot(opcode, register, pointPile):		#4XNN si vx != nn saut instruc suiv
	val = (opcode & 0x0F00) >> 8
	if register[val] != (opcode & 0x00FF):
		pointPile += 2
		return pointPile

def nextReg(opcode, register, pointPile):		#5XY0 si vx = vy saut instruc suiv
	vx = (opcode & 0x0F00) >> 8
	vy = (opcode & 0x00F0) >> 4
	if register[vx] == register[vy]:
		pointPile += 2
		return pointPile

def setNnVx(opcode, register):					#6XNN definit vx à nn
	vx = (opcode & 0x0F00) >> 8
	register[vx] = (opcode & 0x00FF)
	return register

def addNnVx(opcode, register):					#7XNN vx + nn
	vx = (opcode & 0x0F00) >> 8
	operation = register[vx] + (opcode & 0x00FF)
	if operation > 0x00FF:
		operation &= 0x00FF
	register[vx] = operation
	return register

def setVxVy(opcode, register):					#8XY0 definit vx à vy
	vx = (opcode & 0x0F00) >> 8
	vy = (opcode & 0x00F0) >> 4
	register[vx] = register[vy]
	return register

def setVxOrVy(opcode, register):				#8XY1 définit vx à vx "or" vy
	vx = (opcode & 0x0F00) >> 8
	vy = (opcode & 0x00F0) >> 4
	register[vx] |= register[vy]
	return register

def setVxAndVy(opcode, register):				#8XY3 définit vx à vx "and" vy
	vx = (opcode & 0x0F00) >> 8
	vy = (opcode & 0x00F0) >> 4
	register[vx] &= register[vy]
	return register

def setVxXorVy(opcode, register):				#8XY3 définit vx à vx "xor" vy
	vx = (opcode & 0x0F00) >> 8
	vy = (opcode & 0x00F0) >> 4
	register[vx] ^= register[vy]
	return register

def addVyVx(opcode, register):					#8XY4 additionne vy à vx, vf passe à 1 si dépassement memoire
	vx = (opcode & 0x0F00) >> 8
	vy = (opcode & 0x00F0) >> 4
	operation = register[vx] + register[vy]
	if operation > 0x00FF:
		operation &= 0x00FF
		register[0xF] = 1
	else
		register[0xF] = 0
	register[vx] = operation
	return register

def subVyVx(opcode, register):					#8XY5 soustrait vy de vx, vf passe à 0 quand vx < 0
	vx = (opcode & 0x0F00) >> 8
	vy = (opcode & 0x00F0) >> 4
	operation = register[vx]
	if operation < register[vy]:
		operation = 0x00FF + operation - register[vy]
		register[0xF] = 0
	else
		operation = register[vx] - register[vy]
		register[0xF] = 1
		register[vx] = operation
	return register

def decVxRight(opcode, register):				#8XY6 décale vx à droite de 1bit, init vf = bit poid faible vx
	val = bin(registre[(opcode & 0x0F00) >> 8])[-1]
	register[0xF] = val
	vx = (opcode & 0x0F00) >> 8
	register[vx] = register[vx] >> 1
	return register

def subVxVy(opcode, register):					#8XY7 vx = vy - vx, vf passe à 0 quand vx < 0
	vx = (opcode & 0x0F00) >> 8
	vy = (opcode & 0x00F0) >> 4
	operation = register[vy]
	if operation < register[vx]:
		operation = 0x00FF + operation - register[vx]
		register[0xF] = 0
	else
		operation = register[vy] - register[vx]
		register[0xF] = 1
		register[vx] = operation
	return register

def decVxLeft(opcode, register):				#8XYE décale vx à gauche de 1bit, init vf = bit poid fort vx
	val = bin(registre[(opcode & 0x0F00) >> 8])[2]
	register[0xF] = val
	vx = (opcode & 0x0F00) >> 8
	register[vx] = register[vx] << 1
	return register

def jmpIfVxNoVy(opcode, register, pointPile):	#9XY0 saute l'instruction suiv si  vx != vy
	vx = (opcode & 0x0F00) >> 8
	vy = (opcode & 0x00F0) >> 4
	if register[vx] != register[vy]:
		pointPile += 2
		return pointPile

def nnnI(opcode, register, regI):				#ANNN affecte nnn à regI
	regI = opcode & 0xFFF
	return regI

def nnnVo(opcode, register, pointPile):			#BNNN pass à l'adresse nnn + v0
	pointPile = (opcode & 0xFFF) + register[0]
	return pointPile

def rndVx(opcode, register):					#CXNN définit vx à un nombre aléatoire < 255 et > 0
	vx = (opcode & 0x0F00) >> 8
	register[vx] = randint(0,255) & (opcode & 0x00FF)
	return register

def sprite(opcode, register, ):					#DXYN fait un sprite aux coordonnées (VX, VY)



def keyVxYes(opcode, register):					#EX9E si clé dans vx pressée instuction suivante

def keyVxNo(opcode, register):					#EXA1 si clé dans vx non pressée instruc suivante

def tmpVx(opcode, register, delay):				#FX07 définit vx à la valeur de la temporisation
	vx = (opcode & 0x0F00) >> 8
	register[vx] = delay
	return register

def key(opcode, register):						#FX0A attend le signal d'une touche et la stock dans vx
    vx = (opcode & 0x0F00) >> 8
    key = False
#    while not key:
#        event = pygame.event.wait()
#        if event.type == pygame.KEYDOWN:
#            key = key.get_pressed()
#            for keyval, lookup_key in KEY_MAPPINGS.items():
#                if key[lookup_key]:
#                    self.registers['v'][vx] = keyval
#                    key = True
#                    break

def vxTmp(opcode, register, delay):				#FX15 définit tempo à vx
	vx = (opcode & 0x0F00) >> 8
	delay = register[vx]
	return delay

def soundVx(opcode, register, sound):			#FX18 définit minuterie sonore à vx
	vx = (opcode & 0x0F00) >> 8
	sound = register[vx]
	return sound

def addIVx(opcode, register, regI):				#FX1E ajoute regI au registe[vx], vf = 1 si dépassement
	vx = (opcode & 0x0F00) >> 8
	operation = regI + register[vx]
	if operation > 0xFFF:
		operation = operation & 0xFFF
		register[0xf] = 1
	else
		register[0xf] = 0
	regI = operation
	return regI, register

def IdgtVx(opcode, register, regI):				#FX29 définit regI au caractère stocké dans vx
	vx = (opcode & 0x0F00) >> 8
	regI = register[vx] * 5
	return regI

def stkVxI(opcode, register, regI, memory):		#FX33 stock le code decimal de vx dans I,I+1,I+2
	vx = (opcode & 0x0F00) >> 8
	memory[regI] = int(register[vx] // 100)
	memory[regI + 2] = int(register[vx] % 10)
	memory[regI + 1] = int ((register[vx] / 10) % 10)
	return memory

def stkVoVx(opcode, register, regI, memory):	#FX55 stock v0 à vx à partir de l'adresse regI
	vx = (opcode & 0x0F00) >> 8
	i = 0
	while i <= vx:
		memory[regI + i] = register[i]
		i += 1
	return memory

def repVoVx(opcode, register, regI, memory):	#FX65 remplit v0 à vx avec val mem à partir de regI
	vx = (opcode & 0x0F00) >> 8
	i = 0
	while i <= vx:
		register[i] = memory[regI + i]
		i += 1
	return memory
