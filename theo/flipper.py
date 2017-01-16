#!/usr/bin/env python3.5
import pygame
from pygame.locals import *
from math import *
pygame.init()


fenetre = pygame.display.set_mode((800,600), RESIZABLE)

fond = pygame.image.load("fond.jpg").convert()

fond1 = pygame.image.load("backround.jpg").convert()

bordure = pygame.image.load("Contour.png").convert_alpha()

couloir = pygame.image.load("couloir.png").convert_alpha()

balle = pygame.image.load("balle.png").convert_alpha()
position_balle = balle.get_rect()

Trileft = pygame.image.load("TriangleLeft.png").convert_alpha()

Triright = pygame.image.load("Triangleright.png").convert_alpha()

left = pygame.image.load("left.png").convert_alpha()

right = pygame.image.load("right.png").convert_alpha()

pygame.display.flip()



continuer = 1
x, y = 589, 480
position_balle = (x, y)
Pfond = (0,0)
Pfond1 = (213, 0)
Pbordure = (213, 0)
Pcouloir = (580, 225)
Ptrileft = (213,415)
Ptriright = (519,443)
Pleft = (173,350)
Pright = (433,430)

def aff():
	fenetre.blit(fond, Pfond)
	fenetre.blit(fond1, Pfond1)
	fenetre.blit(bordure, Pbordure)
	fenetre.blit(couloir, Pcouloir)
	fenetre.blit(Trileft, Ptrileft)
	fenetre.blit(Triright, Ptriright)
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
			if event.key == K_DOWN:	#Si "flèche bas On descend le perso"
				y = y + 20
				position_balle = (x, y)
			if event.key == K_UP:	#Si "flèche bas On descend le perso"
				y = y - 20	
				position_balle = (x, y)
			if event.key == K_RIGHT:	#Si "flèche bas On descend le perso"
				x = x + 20
				position_balle = (x, y)
			if event.key == K_LEFT:	#Si "flèche bas On descend le perso"
				x = x - 20
				position_balle = (x, y)
			while pygame.key.get_pressed()[K_a]:
				left = pygame.transform.rotate(left, 90)
				aff()
				#pygame.time.wait(200)
				left = pygame.transform.rotate(left, 270)
				aff()
			if event.key == K_z:
				right = pygame.transform.rotate(right, 270)
				aff()
				pygame.time.wait(200)
				right = pygame.transform.rotate(right, 90)
				aff()
