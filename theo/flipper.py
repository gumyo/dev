#!/usr/bin/env python3.5
import pygame
from pygame.locals import *
from math import *
pygame.init()


fenetre = pygame.display.set_mode((800,600), RESIZABLE)

fond = pygame.image.load("fond.jpg").convert()

fond1 = pygame.image.load("backround.jpg").convert()

balle = pygame.image.load("balle.png").convert_alpha()
position_balle = balle.get_rect()

left = pygame.image.load("left.png").convert_alpha()

right = pygame.image.load("right.png").convert_alpha()

pygame.display.flip()



continuer = 1
x, y = 589, 480
position_balle = (x, y)
Pfond = (0,0)
Pfond1 = (213, 0)
Pleft = (173,350)
Pright = (433,430)

def aff():
	fenetre.blit(fond, Pfond)
	fenetre.blit(fond1, Pfond1)
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
			if event.key == K_a:
				left = pygame.transform.rotate(left, 90)
			if event.key == K_z:
				right = pygame.transform.rotate(right, 270)

		elif event.type == KEYUP:
			if event.key == K_a:
				left = pygame.transform.rotate(left, 270)

			if event.key == K_z:
				right = pygame.transform.rotate(right, 90)