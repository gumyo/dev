#!/usr/bin/env python3.5
import pygame
from pygame.locals import *
from math import *
pygame.init()


fenetre = pygame.display.set_mode((800,600), RESIZABLE)

fond = pygame.image.load("fond.jpg").convert()

fond1 = pygame.image.load("backround.png").convert()

contour = pygame.image.load("contour.png").convert_alpha()

balle = pygame.image.load("balle.png").convert_alpha()
position_balle = balle.get_rect()

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

pygame.display.flip()



continuer = 1
x, y = 585, 490
position_balle = (585, 380)
Pfond = (0,0)
Pfond1 = (213, 0)
Pcontour = (213, 0)
Pleft = (180,380)
Pright = (322,382)
Prampe = (575, 180)
Pcache = (577, 523)
Pcouloir = (575, 177)
Ppoussoir = (x, y)
Pporte_couloir = (573, 185)
Pstar = (557, 500)
Pstar_socle = (557, 520)
Pobsright = (528, 203)
Pobsleft = (228	, 285)
press = pygame.key.set_repeat(1,1000)

def aff():
	fenetre.blit(fond, Pfond)
	fenetre.blit(fond1, Pfond1)
	fenetre.blit(contour, Pcontour)
	fenetre.blit(couloir, Pcouloir)
	fenetre.blit(rampe, Prampe)
	fenetre.blit(poussoir, Ppoussoir)
	fenetre.blit(cache, Pcache)
	fenetre.blit(obstacle_right, Pobsright)
	fenetre.blit(obstacle_left, Pobsleft)
	fenetre.blit(porte_couloir, Pporte_couloir)
	fenetre.blit(star, Pstar)
	fenetre.blit(star_socle, Pstar_socle)
	fenetre.blit(Item_raquette_droite, (485, 437))
	fenetre.blit(Top_droite, (520, 365))
	fenetre.blit(Bloqueur_droit, (480, 430))
	fenetre.blit(Bloqueur_gauche, (295, 430))
	fenetre.blit(Item_raquette_gauche, (250, 420))
	fenetre.blit(barrage_gauche, (225, 405))
	fenetre.blit(cible_1, (370, 480))
	fenetre.blit(cible_3, (315, 415))
	fenetre.blit(cible_5, (370, 400))
	fenetre.blit(left, Pleft)
	fenetre.blit(right, Pright)
	fenetre.blit(balle, position_balle)
	pygame.display.flip()

#Boucle infinie
while continuer:
	aff()
	for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
		if event.type == QUIT:     #Si on clique sur la croix.
			continuer = 0      #On arrête la boucle
		if event.type == KEYDOWN:
			if event.type == KEYDOWN and event.key == K_ESCAPE:     #Si on presse la touche echap
				continuer = 0      #On arrête la boucle
			if event.key == K_a:
				left = pygame.transform.rotate(left, 90)
			if event.key == K_z:
				right = pygame.transform.rotate(right, 270)
			if event.key == K_SPACE:
				press
				y = y+10
				Ppoussoir = (x, y)
		elif event.type == KEYUP:
			if event.key == K_SPACE:
				y = 490
				Ppoussoir = (x, y)
			if event.key == K_a:
				left = pygame.transform.rotate(left, 270)
			if event.key == K_z:
				right = pygame.transform.rotate(right, 90)