#!/usr/bin/env python3
import pygame
from pygame.locals import *
pygame.init()


fenetre = pygame.display.set_mode((800,600), RESIZABLE)

fond = pygame.image.load("fond.jpg").convert()
fenetre.blit(fond, (0,0))

fond1 = pygame.image.load("backround.jpg").convert()
fenetre.blit(fond1, (213,0))

balle = pygame.image.load("balle.png").convert_alpha()
fenetre.blit(balle, (10,100))
position_balle = balle.get_rect()
fenetre.blit(balle, (position_balle))

left = pygame.image.load("left.png").convert_alpha()
fenetre.blit(left, (250,500))

right = pygame.image.load("right.png").convert_alpha()
fenetre.blit(right, (450,500))

pygame.display.flip()

angle = 0
continuer = 1

#Boucle infinie
while continuer:
	for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
		if event.type == QUIT:     #Si on clique sur la croix.
			continuer = 0      #On arrête la boucle
		if event.type == KEYDOWN:
			if event.type == KEYDOWN and event.key == K_ESCAPE:     #Si on presse la touche echap
				continuer = 0      #On arrête la boucle
			if event.key == K_DOWN:	#Si "flèche bas On descend le perso"
				position_balle = position_balle.move(0,20)
			if event.key == K_UP:	#Si "flèche bas On descend le perso"
				position_balle = position_balle.move(0,-20)
			if event.key == K_RIGHT:	#Si "flèche bas On descend le perso"
				position_balle = position_balle.move(20,0)
			if event.key == K_LEFT:	#Si "flèche bas On descend le perso"
				position_balle = position_balle.move(-20,0)
			if event.key == K_a:
				left = pygame.transform.rotate(left, 90)
				fenetre.blit(fond, (0,0))
				fenetre.blit(fond1, (213,0))
				fenetre.blit(left, (250,500))
				fenetre.blit(right, (450,500))
				fenetre.blit(balle, position_balle)
				pygame.display.flip()
				pygame.time.wait(200)
				left = pygame.transform.rotate(left, 270)
				fenetre.blit(fond, (0,0))
				fenetre.blit(fond1, (213,0))
				fenetre.blit(left, (250,500))
				fenetre.blit(right, (450,500))
				fenetre.blit(balle, position_balle)			
				pygame.display.flip()
			if event.key == K_z:
				right = pygame.transform.rotate(right, 270)
				fenetre.blit(fond, (0,0))
				fenetre.blit(fond1, (213,0))
				fenetre.blit(left, (250,500))
				fenetre.blit(right, (450,500))
				fenetre.blit(balle, position_balle)
				pygame.display.flip()
				pygame.time.wait(200)
				right = pygame.transform.rotate(right, 90)
				fenetre.blit(fond, (0,0))
				fenetre.blit(fond1, (213,0))
				fenetre.blit(left, (250,500))
				fenetre.blit(right, (450,500))
				fenetre.blit(balle, position_balle)			
				pygame.display.flip()
	pygame.display.flip()
	fenetre.blit(fond, (0,0))
	fenetre.blit(fond1, (213,0))
	fenetre.blit(left, (250,500))
	fenetre.blit(right, (450,500))
	fenetre.blit(balle, position_balle)
	pygame.display.flip()
