# my_Chip8.py
# émulateur chip8 Python
# nécessite pyglet

import pyglet
import random
import sys
import time

from pyglet.sprite import Sprite

clavSet = {
		pyglet.window.key._1: 0x1,
        pyglet.window.key._2: 0x2,
        pyglet.window.key._3: 0x3,
        pyglet.window.key._4: 0xc,
        pyglet.window.key.A: 0x4,
        pyglet.window.key.Z: 0x5,
        pyglet.window.key.E: 0x6,
        pyglet.window.key.R: 0xd,
        pyglet.window.key.Q: 0x7,
        pyglet.window.key.S: 0x8,
        pyglet.window.key.D: 0x9,
        pyglet.window.key.F: 0xe,
        pyglet.window.key.W: 0xa,
        pyglet.window.key.X: 0,
        pyglet.window.key.C: 0xb,
        pyglet.window.key.V: 0xf
        }

memoire = 4096*[0]
regI = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 
		9: 0, 0xA: 0, 0xB: 0, 0xC: 0, 0xD: 0, 0xE: 0, 0xF: 0}
pile = []
clavIn = 16*[0]
lettres = [
		0xF0, 0x90, 0x90, 0x90, 0xF0, 0x20, 0x60, 0x20, 0x20, 0x70, 
		0xF0, 0x10, 0xF0, 0x80, 0xF0, 0xF0, 0x10, 0xF0, 0x10, 0xF0, 
		0x90, 0x90, 0xF0, 0x10, 0x10, 0xF0, 0x80, 0xF0, 0x10, 0xF0, 
		0xF0, 0x80, 0xF0, 0x90, 0xF0, 0xF0, 0x10, 0x20, 0x40, 0x40, 
		0xF0, 0x90, 0xF0, 0x90, 0xF0, 0xF0, 0x90, 0xF0, 0x10, 0xF0, 
		0xF0, 0x90, 0xF0, 0x90, 0x90, 0xE0, 0x90, 0xE0, 0x90, 0xE0, 
		0xF0, 0x80, 0x80, 0x80, 0xF0, 0xE0, 0x90, 0x90, 0x90, 0xE0,
        0xF0, 0x80, 0xF0, 0x80, 0xF0, 0xF0, 0x80, 0xF0, 0x80, 0x80 
        ]

tblFnc = None
opCode = 0
index = 0
contProg = 0
affich = 32*64*[0]
delTmp = 0
sonTmp = 0
dessin = False
clavAtt = False
pixel = pyglet.resource.image("pixel.png")
bip = pyglet.resource.media('buzz.wav', streaming=False)
pixBuff = pyglet.graphics.Batch()
pixi = []
for i in range(0,2048):
	pixi.append(pyglet.sprite.Sprite(pixel,batch=pixBuff))

vx = (opCode & 0x0F00) >> 8
vy = (opCode & 0x00F0) >> 4


def non1(opCode, tblFnc):
	opera = opCode & 0xF0FF
	try:
		tblFnc[opera]()
	except:
		print ("instruction inconnue: %x" % opCode)
	return 0

def cls(affich, dessin)
	affich = 32*64*[0]
	dessin = True
	return affich, dessin


def ret(contProg, pile):						# retourne à la sous fonction
	contProg = pile.pop()
	return contProg

def jump(opCode, contProg):						#1NNN saute à l'adresse nnn
	contProg = opCode & 0x0FFF
	return contProg

def call(opCode, contProg, pile):				#2NNN Exec sous programme de nnn
	pile.append(contProg)
	contProg = opCode & 0x0FFF
	return contProg, pile

def nextNn(opCode, contProg, regI, vx):			#3XNN si vx = nn on saut instruction suiv
	if regI[vx] == (opCode & 0x00FF):
		contProg = contProg + 2
	return contProg

def nextNo(opCode, contProg, regI, vx):
	if regI[vx] != (opCode & 0x00FF):
		contProg = contProg + 2
	return contProg

def nextVy(contProg, regI, vx, vy):
	if regI[vx] == regI[vy]:
		contProg = contProg + 2
	return contProg

def stVxNn(opCode, regI, vx):
	regI[vx] = opCode & 0x00FF
	return regI

def adNnVx(opCode, regI, vx):
	regI[vx] = regI[vx] + (opCode & 0xFF)
	return regI

def non2(opCode, tblFnc):
	opera = opCode & 0xF00F
	opera += 0xFF0
	try:
		tblFnc[opera]()
	except:
		print ("instruction inconnue: %x" % opCode)

def stVxVy(regI, vx, vy):
	regI[vx] = regI[vy]
	regI[vx] &= 0xFF
	return regI

def vxOuVy(regI, vx, vy):
	regI[vx] |= regI[vy]
	regI[vx] &= 0xFF
	return regI

def vxEtVy(regI, vx, vy):
	regI[vx] &= regI[vy]
	regI[vx] &= 0xFF
	return regI

def vXorVy(regI, vx, vy):
	regI[vx] ^= regI[vy]
	regI[vx] &= 0xFF
	return regI

def adVxVy(regI, vx, vy):
	if regI[vx] + regI[vy] > 0xFF:
		regI[0xF] = 1
	else:
		regI[0xF] = 0
	regI[vx] += regI[vy]
	regI[vx] &= 0xFF
	return regI

def suVxVy(regI, vx, vy):
	if regI[vy] > regI[vx]:
		regI[0xF] = 0
	else:
		regI[0xF] = 1
	regI[vx] = regI[vx] - regI[vy]
	regI[vx] &= 0xFF
	return regI

def mvVxD(regI, vx, vy):
	regI[0xF] = regI[vx] & 0x0001
	regI[vx] = regI[vx] >> 1
	return regI

def suVyVx(regI, vx, vy):
	if regI[vx] > regI[vy]:
		regI[0xF] = 0
	else:
		regI[0xF] = 1
	regI[vx] = regI[vy] - regI[vx]
	regI[vx] &= 0xFF
	return regI

def mvVxG(regI, vx, vy):
	regI[0xF] = (regI[vx] & 0x00F0) >> 7
	regI[vx] = regI[vx] << 1
	regI[vx] &= 0xFF
	return regI

def pasVx(contProg, regI, vx, vy):
	if regI[vx] != regI[vy]:
		contProg = contProg + 2
	return contProg

def nnnI(opCode, index):
	index = opCode & 0x0FFF

def jmpNnn(opCode, contProg, regI):
	contProg = (opCode & 0x0FFF) + regI[0]

