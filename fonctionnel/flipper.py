#!/usr/bin/env python3.5
import pygame
from pygame.locals import *
from math import *
import math
import time
pygame.init()


fenetre = pygame.display.set_mode((800,600), RESIZABLE)

fond = pygame.image.load("fond.jpg").convert()

fond1 = pygame.image.load("backround.png").convert()

contour = pygame.image.load("contour.png").convert_alpha()

balle = pygame.image.load("balle.png").convert_alpha()

rampe = pygame.image.load("rampe.png").convert_alpha()

couloir = pygame.image.load("FondCOULOIR.png").convert_alpha()

poussoir = pygame.image.load("Poussoir.png").convert_alpha()

porte_couloir = pygame.image.load("PorteCouloir.png").convert_alpha()

cache = pygame.image.load("CacheDuPOUSSOIR.png").convert_alpha()

star = pygame.image.load("star.png").convert_alpha()

star_socle = pygame.image.load("StarSOCLE.png").convert_alpha()

Item_raquette_droite = pygame.image.load("Item_raquette_droite.png").convert_alpha()

obstacle_right = pygame.image.load("obstacleRigth.png").convert_alpha()

obstacle_left = pygame.image.load("obstacleLeft.png").convert_alpha()

Top_droite = pygame.image.load("Top_A_Droite.png").convert_alpha()

Bloqueur_droit = pygame.image.load("bloqueurDroit.png").convert_alpha()

Bloqueur_gauche = pygame.image.load("bloqueurGauche.png").convert_alpha()

Item_raquette_gauche = pygame.image.load("Item_raquette_gauche.png").convert_alpha()

barrage_gauche = pygame.image.load("Barage_raquette.png").convert_alpha()

cible_1 = pygame.image.load("cible_X1.png").convert_alpha()

cible_3 = pygame.image.load("cible_X3.png").convert_alpha()

cible_5 = pygame.image.load("cible_X5.png").convert_alpha()

left = pygame.image.load("left.png").convert_alpha()

right = pygame.image.load("right.png").convert_alpha()

bumper_un = pygame.image.load("Bumper_un.png").convert_alpha()

bumper_deux = pygame.image.load("Bumper_quatre_gros.png").convert_alpha()

bumper_trois = pygame.image.load("Bumper_trois_central.png").convert_alpha()

bumper_quatre = pygame.image.load("Bumper_deux.png").convert_alpha()

bumper_cinq = pygame.image.load("Bumper_cinq.png").convert_alpha()

petitbarrage = pygame.image.load("petitBarage.png").convert_alpha()

Cchambre = pygame.image.load("ContourChambre.png").convert_alpha()

Echambre = pygame.image.load("interieurChambre.png").convert_alpha()

pygame.display.flip()

#(585, 380)

continuer = 1
x, y = 585, 490
press = pygame.key.set_repeat(1,1000)
mouv = balle.get_rect()
mouv.x = 586
mouv.y = 479
perm = False
collision = False
compteur = 0
temps = 0
dep = 200
def aff():
	fenetre.blit(fond, (0,0))
	fenetre.blit(fond1, (213, 0))
	fenetre.blit(contour, (213, 0))
	fenetre.blit(couloir, (575, 177))
	fenetre.blit(rampe, (575, 180))
	fenetre.blit(poussoir, (x, y))
	fenetre.blit(cache, (577, 523))
	fenetre.blit(obstacle_right, (528, 203))
	fenetre.blit(obstacle_left, (228, 285))
	fenetre.blit(porte_couloir, (573, 185))
	fenetre.blit(star, (557, 500))
	fenetre.blit(star_socle, (557, 520))
	fenetre.blit(Item_raquette_droite, (485, 437))
	fenetre.blit(Top_droite, (520, 365))
	fenetre.blit(Bloqueur_droit, (480, 430))
	fenetre.blit(Bloqueur_gauche, (295, 430))
	fenetre.blit(Item_raquette_gauche, (250, 420))
	fenetre.blit(barrage_gauche, (225, 405))
	fenetre.blit(bumper_un, (460, 300))
	fenetre.blit(bumper_deux, (390, 300))
	fenetre.blit(bumper_trois, (460, 230))
	fenetre.blit(bumper_quatre, (530, 185))
	fenetre.blit(bumper_cinq, (410, 190))
	fenetre.blit(petitbarrage, (385	, 230))
	fenetre.blit(Cchambre, (250, 100))
	fenetre.blit(Echambre, (285, 100))
	fenetre.blit(cible_1, (370, 480))
	fenetre.blit(cible_3, (335, 435))
	fenetre.blit(cible_5, (370, 400))
	fenetre.blit(left, (180,380))
	fenetre.blit(right, (322,382))
	fenetre.blit(balle, mouv)
	pygame.display.flip()

#5, 0, 39 (bleu)
#149, 54, 57 (rose)
def mouvv(mouv, dep):
	global perm, collision
	test = fenetre.get_at((mouv.x, mouv.y))
	alpha = 1
	if test == (5, 0, 39, 255) or test == (149, 54, 57, 255):
		grou = False
		if perm == True:
			perm = False
			collision = True
			alpha = 50
		else:
			perm = False
			collision = True
			alpha = 80
	if collision:
		dep += 100
		alpha = -1
		mouv.y +=1 * math.sin(alpha)
		mouv.x -=1 * math.cos(alpha)
	#couleur_position_balle = int('%02x%02x%02x' % (r1, g1, b1), 16)
	if perm:
		mouv.y -=1 * math.sin(alpha)
		mouv.x +=1 * math.cos(alpha)
	return mouv


while continuer:
	aff()
	mouvv(mouv, dep)
	pygame.time.Clock().tick(dep)
	for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
		if event.type == QUIT:     #Si on clique sur la croix.
			continuer = 0      #On arrête la boucle
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:     #Si on presse la touche echap
				continuer = 0      #On arrête la boucle
			if event.key == K_a:
				left = pygame.transform.rotate(left, 90)
			if event.key == K_z:
				right = pygame.transform.rotate(right, 270)
			if event.key == K_SPACE:
				press
				perm = False
				y += 10
				Ppoussoir = (x, y)
		elif event.type == KEYUP:
			if event.key == K_SPACE:
				perm = True
				y = 490
				Ppoussoir = (x, y)
			if event.key == K_a:
				left = pygame.transform.rotate(left, 270)
			if event.key == K_z:
				right = pygame.transform.rotate(right, 90)