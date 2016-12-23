#!/usr/bin/env python3
import pygame
from pygame.locals import *
pygame.init()


fenetre = pygame.display.set_mode((640,480), RESIZABLE)

fond = pygame.image.load("fond.jpg").convert()
fenetre.blit(fond, (0,0))

fond1 = pygame.image.load("backround.jpg").convert()
fenetre.blit(fond1, (213,160))

perso = pygame.image.load("balle.jpg").convert()
perso.set_colorkey((255,255,255))
position_perso = perso.get_rect()
fenetre.blit(perso, position_perso)

pygame.display.flip()


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
				position_perso = position_perso.move(0,20)
			if event.key == K_UP:	#Si "flèche bas On descend le perso"
				position_perso = position_perso.move(0,-20)
			if event.key == K_RIGHT:	#Si "flèche bas On descend le perso"
				position_perso = position_perso.move(20,0)
			if event.key == K_DOWN:	#Si "flèche bas On descend le perso"
				position_perso = position_perso.move(-20,0)
	fenetre.blit(fond, (0,0))
	fenetre.blit(fond1, (213,160))
	fenetre.blit(perso, position_perso)
	pygame.display.flip()