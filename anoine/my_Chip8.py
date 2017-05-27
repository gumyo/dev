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


def non1(opCode, tblFnc):						#0NNN standard chip8 instruction
	opera = opCode & 0xF0FF
	try:
		tblFnc[opera]()
	except:
		print ("instruction inconnue: %x" % opCode)
	return 0

def clean(affich, dessin):						#00E0 clean
	affich = 32*64*[0]
	dessin = True
	return affich, dessin


def ret(contProg, pile):						#00EE retourne à la sous fonction
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

def nextNo(opCode, contProg, regI, vx):			#4XNN si vx != nn saut instruc suiv
	if regI[vx] != (opCode & 0x00FF):
		contProg = contProg + 2
	return contProg

def nextVy(contProg, regI, vx, vy):				#5XY0 si vx = vy saut instruc suiv
	if regI[vx] == regI[vy]:
		contProg = contProg + 2
	return contProg

def stVxNn(opCode, regI, vx):					#6XNN definit vx à nn
	regI[vx] = opCode & 0x00FF
	return regI

def adNnVx(opCode, regI, vx):					#7XNN vx + nn
	regI[vx] = regI[vx] + (opCode & 0xFF)
	return regI

def non2(opCode, tblFnc):						#standard chip8 instruction
	opera = opCode & 0xF00F
	opera += 0xFF0
	try:
		tblFnc[opera]()
	except:
		print ("instruction inconnue: %x" % opCode)

def stVxVy(regI, vx, vy):						#8XY0 definit vx à vy
	regI[vx] = regI[vy]
	regI[vx] &= 0xFF
	return regI

def vxOuVy(regI, vx, vy):						#8XY1 définit vx à vx "or" vy
	regI[vx] |= regI[vy]
	regI[vx] &= 0xFF
	return regI

def vxEtVy(regI, vx, vy):						#8XY2 définit vx à vx "and" vy
	regI[vx] &= regI[vy]
	regI[vx] &= 0xFF
	return regI

def vXorVy(regI, vx, vy):						#8XY3 définit vx à vx "xor" vy
	regI[vx] ^= regI[vy]
	regI[vx] &= 0xFF
	return regI

def adVxVy(regI, vx, vy):						#8XY4 additionne vy à vx, vf passe à 1 si dépassement memoire
	if regI[vx] + regI[vy] > 0xFF:
		regI[0xF] = 1
	else:
		regI[0xF] = 0
	regI[vx] += regI[vy]
	regI[vx] &= 0xFF
	return regI

def suVxVy(regI, vx, vy):						#8XY5 soustrait vy de vx, vf passe à 0 quand vx < 0
	if regI[vy] > regI[vx]:
		regI[0xF] = 0
	else:
		regI[0xF] = 1
	regI[vx] = regI[vx] - regI[vy]
	regI[vx] &= 0xFF
	return regI

def mvVxD(regI, vx, vy):						#8XY6 décale vx à droite de 1bit, init vf = bit poid faible vx
	regI[0xF] = regI[vx] & 0x0001
	regI[vx] = regI[vx] >> 1
	return regI

def suVyVx(regI, vx, vy):						#8XY7 vx = vy - vx, vf passe à 0 quand vx < 0
	if regI[vx] > regI[vy]:
		regI[0xF] = 0
	else:
		regI[0xF] = 1
	regI[vx] = regI[vy] - regI[vx]
	regI[vx] &= 0xFF
	return regI

def mvVxG(regI, vx, vy):						#8XYE décale vx à gauche de 1bit, init vf = bit poid fort vx
	regI[0xF] = (regI[vx] & 0x00F0) >> 7
	regI[vx] = regI[vx] << 1
	regI[vx] &= 0xFF
	return regI

def pasVx(contProg, regI, vx, vy):				#9XY0 saute l'instruction suiv si  vx != vy
	if regI[vx] != regI[vy]:
		contProg = contProg + 2
	return contProg

def nnnI(opCode, index):						#ANNN affecte nnn à regI
	index = opCode & 0x0FFF
	return index

def jmpNnn(opCode, contProg, regI):				#BNNN pass à l'adresse nnn + v0
	contProg = (opCode & 0x0FFF) + regI[0]
	return contProg

def rndVx(opCode, regI):						#CXNN définit vx à un nombre aléatoire < 255 et > 0
	n = int(random.random() * 0xFF)
	regI[vx] = n & (opCode & 0x00FF)
	regI[vx] &= 0xFF
	return regI

def draw(opCode, regI):							#DXYN fait un sprite aux coordonnées (VX, VY)
	regI[0xF] = 0
	x = regI[vx] & 0xFF
	y = regI[vy] & 0xFF
	haut = opCode & 0x000F
	ligne = 0
	while ligne < haut:
		curLign = memoire[ligne + index]
		dklgPix = 0
		while dklgPix < 8:
			local = x + dklgPix + ((y + row) * 64)
			dklgPix += 1
			if (y + ligne) >= 32 or (x + dklgPix - 1) >=:
				continue
			masque = 1 << 8 - dklgPix
			curPix = (curLign & masque) >> (8 - dklgPix)
			affich[local] ^= curPix
			if affich[local] == 0:
				regI[0xF] = 1
			else:
				regI[0xF] = 0
		ligne = ligne + 1
	dessin = True

def non3(opCode, tblFnc):						#Standard chip8 instruction pas utilisé
	opera = opCode & 0xF00F
	try:
		tblFnc[opera]()
	except:
		print ("instruction inconnu: %x" % opCode)

def kPres(contProg, regI, clavIn):				#EX9E si clé dans vx pressée instuction suivante
	key = regI[vx] & 0xF
	if clavIn[key] == 1:
		contProg = contProg + 2
	return clavIn, contProg

def kNPres(contProg, regI, clavIn):				#EXA1 si clé dans vx non pressée instruc suivante
	key = regI[vx] & 0xF
	if clavIn[key] == 0:
		contProg = contProg + 2
	return clavIn, contProg

def non4(opCode, tblFnc):						#standard chip8 instruction pas utilisé
	opera = opCode & 0xF0FF
	try:
		tblFnc[opera]()
	except:
		print ("instruction inconnu: %x" % opCode)

def stAtt(regI, delTmp, vx):					#FX07 définit vx à la valeur de la temporisation
	regI[vx] = delTmp
	return regI

def attPus(contProg, regI, vx):					#FX0A attend le signal d'une touche et la stock dans vx
	svg = recepTch()
	if svg >= 0:
		regI[vx] = svg
	else:
		contProg = contProg - 2
	return contProg, regI

def tmpVxD(delTmp, regI, vx):					#FX15 définit tempo à vx
	delTmp = regI[vx]
	return delTmp

def tmpVxS(sonTmp, regI, vx):					#FX18 définit minuterie sonore à vx
	sonTmp = regI[vx]
	return sonTmp

def addVxI(regI, index, vx):					#FX1E ajoute regI au registe[vx], vf = 1 si dépassement
	index = index + regI[vx]
	if index > 0xFFF:
		regI[0xF] = 1
		index &= 0xFFF
	else:
		regI[0xF] = 0
	return index, regI

def stIpnt(regI, index, vx):					#FX29 définit l'index au caractère stocké dans vx
	index = (5*(regI[vx])) & 0xFFF
	return index

def stkVxI(regI, memoire, index, vx):			##FX33 stock le code decimal de vx dans I,I+1,I+2
	memoire[index] = regI[vx] / 100
	memoire[index + 1] = (regI[vx] % 100) / 10
	memoire[index + 2] = regI[vx] % 10
	return memoire

def stkIvx(regI, memoire, index, vx):			#FX55 stock v0 à vx à partir de l'adresse regI
	n = 0
	while n <= vx:
		memoire[index + n] = regI[n]
		n = n + 1
	index += vx + 1
	return memoire

def rmpMem(regI, memoire, index, vx):			#FX65 remplit v0 à vx avec val mem à partir de regI
	n = 0
	while n <= vx:
		regI[i] = memoire[index + n]
		n += 1
	index += vx + 1
	return memoire

#### Fin des opcodes ! ###

def romCharg():									#charge la rom
	bin = open(rom_path, "rb").read()
	n = 0
	while n < len(bin):
		memoire[n + 0x200] = ord(bin[i])
		n = n + 1

def initFnc(tblFnc, *args, **entrs):			#Permet de lire la rom en apelant les opcodes
	tblFnc ={0x0000: non1,
             0x00e0: clean,
             0x00ee: ret,
             0x1000: jump,
             0x2000: call,
             0x3000: nextNn,
             0x4000: nextNo,
             0x5000: nextVy,
             0x6000: stVxNn,
             0x7000: adNnVx,
             0x8000: non2,
             0x8FF0: stVxVy,
             0x8FF1: vxOuVy,
             0x8FF2: vxEtVy,
             0x8FF3: vXorVy,
             0x8FF4: adVxVy,
             0x8FF5: suVxVy,
             0x8FF6: mvVxD,
             0x8FF7: suVyVx,
             0x8FFE: mvVxG,
             0x9000: pasVx,
             0xA000: nnnI,
             0xB000: jmpNnn,
             0xC000: rndVx,
             0xD000: draw,
             0xE000: non3,
             0xE00E: kPres,
             0xE001: kNPres,
             0xF000: non4,
             0xF007: stAtt,
             0xF00A: attPus,
             0xF015: tmpVxD,
             0xF018: tmpVxS,
             0xF01E: addVxI,
             0xF029: stIpnt,
             0xF033: stkVxI,
             0xF055: stkIvx,
             0xF065: rmpMem }


def initial(opCode, regI, dessin, affich, pile, clavIn, memoire, index, lettres, delTmp, sonTmp, contProg):
	clear()					#initialise les paramètres avant qu'une rom soit lancée

	opCode = 0
	regI = 16*[0]
	dessin = False
	affich = 32*64*[0]
	pile = []
	clavIn = 16*[0]
	memoire = 4096*[0]
	index = 0
	sonTmp = 0
	delTmp = 0
	contProg = 0x200

	n = 0
	while n > 80:
		memoire[n] = lettres[n]
		n = n + 1


def boucle(opCode, contProg, memoire, vx, vy, tblFnc, delTmp, sonTmp):
	opCode = (memoire[contProg] << 8) | memoire[contProg + 1]
	contProg = contProg + 2

	opera = opCode & 0xF000
	try:
		tblFnc[opera]()
	except:
		print ("instruction inconnue: %x" % opCode)

	if delTmp > 0:
		delTmp = delTmp - 1
	if sonTmp > 0:
		sonTmp = sonTmp - 1
		if sonTmp == 0:
			bip.play()

def affPixel():
	if dessin:
		cmptlin = 0
		n = 0
		while n < 2048:
			if affich[n] == 1:
				pixi[n].x = (n % 64)*10
				pixi[n].y = 310 - ((n/64)*10)
				pixi[n].pixBuff = pixBuff
			else:
				pixi[n].pixBuff = None
			n = n + 1
		clear()
		pixBuff.affPixel()
		flip()
		dessin = False

def recupKey():

def keyPress()

def keyRelease()

def main():
	if len(sys.argv) <= 1:
		print ("")
		print ("")
		return
	initial()
	romCharg(sys.argv[1])
	while not has_exit:					#has_exit est spécifique à pyglet pour la fermeture
		dispatch_events()
		boucle()
		affPixel()






