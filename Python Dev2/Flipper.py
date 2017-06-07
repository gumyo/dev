__version__ = "$Id:$"
__docformat__ = "reStructuredText"

# todo : Enlever les import inutile

import random
import sys, random

import math
import time
from math import sqrt
from math import cos
from math import sin
from math import acos
from math import pi

import pygame
from pygame.locals import *
import datetime

# Initialisation de la fenêtre de jeu
pygame.init()
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption('Flipper')

# Splash screen

fontObj = pygame.font.Font('Cokelines.ttf', 40)
pygame.draw.rect(screen, [255, 255, 255], (0, 0, 1000, 600))
screen.blit(fontObj.render('Chargement 00%', True, (0, 0, 0), None), (350, 250))
pygame.display.flip()

import pymunk
from pymunk import Vec2d
import pymunk.pygame_util

pygame.draw.rect(screen, [255, 255, 255], (0, 0, 1000, 600))
screen.blit(fontObj.render('Chargement 10%', True, (0, 0, 0), None), (350, 250))
pygame.display.flip()

### Chargement des images ###

Images = {}

# Images Mode Kawai et Creepy

for mode in ['Kawai', 'Creepy']:
    Images[mode + 'Background'] = pygame.image.load(mode + "/Background.jpg")
    Images[mode + 'Balle'] = pygame.image.load(mode + "/Balle.png")
    Images[mode + 'Barrage2'] = pygame.image.load(mode + "/Barrage2.png")
    Images[mode + 'BarrageCouloir'] = pygame.image.load(mode + "/BarrageCouloir.png")
    Images[mode + 'Cache'] = pygame.image.load(mode + "/Cache.png")
    Images[mode + 'gif-off'] = pygame.image.load(mode + "/gif-off.png")
    Images[mode + 'Lanceur'] = pygame.image.load(mode + "/Lanceur.png")
    Images[mode + 'Regles'] = pygame.image.load(mode + "/Regles.jpg")
    Images[mode + 'left'] = pygame.image.load(mode + "/left.png")
    Images[mode + 'right'] = pygame.image.load(mode + "/right.png")
    Images[mode + 'Win'] = pygame.image.load(mode + "/Win.jpg")
    Images[mode + 'Loose'] = pygame.image.load(mode + "/Loose.jpg")
    Images[mode + 'BAide'] = pygame.image.load(mode + "/Boutons/Aide.png")
    Images[mode + 'BAideO'] = pygame.image.load(mode + "/Boutons/AideO.png")
    Images[mode + 'BMenu'] = pygame.image.load(mode + "/Boutons/Menu.png")
    Images[mode + 'BMenuO'] = pygame.image.load(mode + "/Boutons/MenuO.png")
    Images[mode + 'BPause'] = pygame.image.load(mode + "/Boutons/Pause.png")
    Images[mode + 'BPauseO'] = pygame.image.load(mode + "/Boutons/PauseO.png")
    Images[mode + 'BQuitter'] = pygame.image.load(mode + "/Boutons/Quitter.png")
    Images[mode + 'BQuitterO'] = pygame.image.load(mode + "/Boutons/QuitterO.png")
    Images[mode + 'BRestart'] = pygame.image.load(mode + "/Boutons/Restart.png")
    Images[mode + 'BRestartO'] = pygame.image.load(mode + "/Boutons/RestartO.png")
    Images[mode + 'BRestart2'] = pygame.image.load(mode + "/Boutons/Restart2.png")
    Images[mode + 'BRestart2O'] = pygame.image.load(mode + "/Boutons/Restart2O.png")
    Images[mode + 'D'] = pygame.image.load(mode + "/DROP/D.png")
    Images[mode + 'O'] = pygame.image.load(mode + "/DROP/O.png")
    Images[mode + 'P'] = pygame.image.load(mode + "/DROP/P.png")
    Images[mode + 'R'] = pygame.image.load(mode + "/DROP/R.png")
    Images[mode + 'TiretF'] = pygame.image.load(mode + "/FLY/TiretF.png")
    Images[mode + 'TiretL'] = pygame.image.load(mode + "/FLY/TiretL.png")
    Images[mode + 'TiretY'] = pygame.image.load(mode + "/FLY/TiretY.png")
    Images[mode + 'N'] = pygame.image.load(mode + "/NIGHT/N.png")
    Images[mode + 'I'] = pygame.image.load(mode + "/NIGHT/I.png")
    Images[mode + 'G'] = pygame.image.load(mode + "/NIGHT/G.png")
    Images[mode + 'H'] = pygame.image.load(mode + "/NIGHT/H.png")
    Images[mode + 'T'] = pygame.image.load(mode + "/NIGHT/T.png")
    Images[mode + 'TiretA'] = pygame.image.load(mode + "/TiretABCD/TiretA.png")
    Images[mode + 'TiretB'] = pygame.image.load(mode + "/TiretABCD/TiretB.png")
    Images[mode + 'TiretC'] = pygame.image.load(mode + "/TiretABCD/TiretC.png")
    Images[mode + 'TiretD'] = pygame.image.load(mode + "/TiretABCD/TiretD.png")

    for i in range(1, 15):
        Images[mode + 'gif' + str(i)] = pygame.image.load(mode + "/gif-on/" + str(i) + mode + ".png")

pygame.draw.rect(screen, [255, 255, 255], (0, 0, 1000, 600))
screen.blit(fontObj.render('Chargement 30%', True, (0, 0, 0), None), (350, 250))
pygame.display.flip()

for i in range(1, 40):
    Images['Kawaigif-Win' + str(i)] = pygame.image.load('Kawai/gif-Win/winKAWAI_000' + ('0' if i < 10 else '') + str(i) + '.png')

pygame.draw.rect(screen, [255, 255, 255], (0, 0, 1000, 600))
screen.blit(fontObj.render('Chargement 40%', True, (0, 0, 0), None), (350, 250))
pygame.display.flip()

for i in range(1, 40):
    Images['Creepygif-Win' + str(i)] = pygame.image.load('Creepy/gif-Win/WINCreepy_000' + ('0' if i < 10 else '') + str(i) + '.png')

pygame.draw.rect(screen, [255, 255, 255], (0, 0, 1000, 600))
screen.blit(fontObj.render('Chargement 50%', True, (0, 0, 0), None), (350, 250))
pygame.display.flip()

for i in range(1, 40):
    Images['Kawaigif-Loose' + str(i)] = pygame.image.load('Kawai/gif-Loose/LooseKAWAI_000' + ('0' if i < 10 else '') + str(i) + '.png')

pygame.draw.rect(screen, [255, 255, 255], (0, 0, 1000, 600))
screen.blit(fontObj.render('Chargement 60%', True, (0, 0, 0), None), (350, 250))
pygame.display.flip()

for i in range(1, 40):
    Images['Creepygif-Loose' + str(i)] = pygame.image.load('Creepy/gif-Loose/LooseCreepy_000' + ('0' if i < 10 else '') + str(i) + '.png')

pygame.draw.rect(screen, [255, 255, 255], (0, 0, 1000, 600))
screen.blit(fontObj.render('Chargement 70%', True, (0, 0, 0), None), (350, 250))
pygame.display.flip()

# Images Menu

Images['MenuBackground'] = pygame.image.load("Menu/MenuBackground.jpg")
Images['MenuCreepy'] = pygame.image.load("Menu/CreepyMode.png")
Images['MenuCreepyO'] = pygame.image.load("Menu/CreepyModeO.png")
Images['MenuCreepyV'] = pygame.image.load("Menu/CreepyModeV.png")
Images['MenuKawai'] = pygame.image.load("Menu/KawaiMode.png")
Images['MenuKawaiO'] = pygame.image.load("Menu/KawaiModeO.png")
Images['MenuCrossDeblock'] = pygame.image.load("Menu/cross_deblock.png")
Images['MenuCrossRules'] = pygame.image.load("Menu/cross_rules.png")
Images['MenuDeblockBackground'] = pygame.image.load("Menu/Deblock.png")
Images['MenuNon'] = pygame.image.load("Menu/NonDeblock.png")
Images['MenuNonO'] = pygame.image.load("Menu/NonDeblockO.png")
Images['MenuOui'] = pygame.image.load("Menu/OuiDeblock.png")
Images['MenuOuiO'] = pygame.image.load("Menu/OuiDeblockO.png")

pygame.draw.rect(screen, [255, 255, 255], (0, 0, 1000, 600))
screen.blit(fontObj.render('Chargement 75%', True, (0, 0, 0), None), (350, 250))
pygame.display.flip()

### Images Transition ###

for i in range(40):
    Images['Transition' + str(i)] = pygame.image.load('Transition/All_000' + ('0' if i < 10 else '') + str(i) + '.png')

pygame.draw.rect(screen, [255, 255, 255], (0, 0, 1000, 600))
screen.blit(fontObj.render('Chargement 85%', True, (0, 0, 0), None), (350, 250))
pygame.display.flip()

# Fin du chargement des images

### Chargements des Musiques ###

Musiques = {}
Musiques['Opening'] = pygame.mixer.Sound('Musiques/Opening.wav')
Musiques['Transition'] = pygame.mixer.Sound('Musiques/Transition.wav')
for mode in ['Kawai', 'Creepy']:
    Musiques[mode + 'Loose'] = pygame.mixer.Sound('Musiques/' + mode + 'Loose.wav')
    Musiques[mode + 'Win'] = pygame.mixer.Sound('Musiques/' + mode + 'Win.wav')
    Musiques[mode + 'Ingame'] = pygame.mixer.Sound('Musiques/' + mode + 'Ingame.wav')

pygame.draw.rect(screen, [255, 255, 255], (0, 0, 1000, 600))
screen.blit(fontObj.render('Chargement 95%', True, (0, 0, 0), None), (350, 250))
pygame.display.flip()

### Fin du chargement des Musiques ###


def mouvv(mouv, dep):
    global perm, collision
    test = screen.get_at((mouv.x, mouv.y))
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
        mouv.y += 1 * math.sin(alpha)
        mouv.x -= 1 * math.cos(alpha)
    # couleur_position_balle = int('%02x%02x%02x' % (r1, g1, b1), 16)
    if perm:
        mouv.y -= 1 * math.sin(alpha)
        mouv.x += 1 * math.cos(alpha)
    return mouv


############################
############################


# --------------------------#


############################
##### Contour josselin #####

def coordFromAngle(angle, R):
    return [round(R * cos(angle)), round(R * sin(angle))]


def getCoordArray(firstAngle, lastAngle, R):
    lCoord = []
    firstPoint = coordFromAngle(firstAngle, R)
    lastPoint = coordFromAngle(lastAngle, R)
    lCoord.append(firstPoint)
    angle = firstAngle
    increment = 1 / abs(firstPoint[0] - lastPoint[0])
    while angle < lastAngle - increment:
        angle += increment
        lCoord.append(coordFromAngle(angle, R))
    lCoord.append(lastPoint)
    return lCoord


def angleFromCoord(coords, R):
    simpleCoords = [coords[0] / R, coords[1] / R]
    setAngle = acos(simpleCoords[0])
    if simpleCoords[1] >= 0:
        return setAngle
    else:
        return 2 * pi - setAngle


def arcG(A, B, C, body, space, largeur_trait):
    R = sqrt((C[0] - A[0]) ** 2 + (C[1] - A[1]) ** 2)
    A = [A[0] - C[0], A[1] - C[1]]
    B = [B[0] - C[0], B[1] - C[1]]
    firstAngle = angleFromCoord(A, R)
    lastAngle = angleFromCoord(B, R)
    lCoords = getCoordArray(firstAngle, lastAngle, R)
    for i in range(0, len(lCoords) - 1):
        space.add(pymunk.Segment(body, (lCoords[i][0] + C[0], lCoords[i][1] + C[1]),
                                 (lCoords[i + 1][0] + C[0], lCoords[i + 1][1] + C[1]), largeur_trait))


def addSegment(liste, body, space, largeur_trait, bol):
    for i in range(1, len(liste)):
        l = pymunk.Segment(body, liste[i - 1], liste[i], largeur_trait)
        l.elasticity = 0.5
        space.add(l)
    if bol == True:
        l = pymunk.Segment(body, liste[len(liste) - 1], liste[0], largeur_trait)
        l.elasticity = 0.5
        space.add(l)

currentMusic = ''

def stopMusics():
    Musiques['Opening'].stop()
    Musiques['Transition'].stop()
    for m in ['Kawai', 'Creepy']:
        Musiques[m + 'Loose'].stop()
        Musiques[m + 'Win'].stop()
        Musiques[m + 'Ingame'].stop()

def playMusic(menu, mode):
    global currentMusic

    if menu == 0 and currentMusic != 'Opening':
        stopMusics()
        currentMusic = 'Opening'
        Musiques[currentMusic].play(-1)
    if menu == 4 and currentMusic != 'Transition':
        stopMusics()
        currentMusic = 'Transition'
        Musiques[currentMusic].play(-1)
    if menu == 1 and currentMusic != (mode + 'Ingame'):
        stopMusics()
        currentMusic = mode + 'Ingame'
        Musiques[currentMusic].play(-1)
    if menu == 2 and currentMusic != (mode + 'Win'):
        stopMusics()
        currentMusic = mode + 'Win'
        Musiques[currentMusic].play(-1)
    if menu == 3 and currentMusic != (mode + 'Loose'):
        stopMusics()
        currentMusic = mode + 'Loose'
        Musiques[currentMusic].play(-1)



def parse(screen):
    CurrentScore = 0

    mode = 'Kawai'

    pause = False

    file = open('CreepyDeblock.txt', 'r')
    creepydeblock = int(file.readline())
    file.close()

    ### Physics stuff
    space = pymunk.Space()
    space.gravity = (0.0, -800.0)
    draw_options = pymunk.pygame_util.DrawOptions(screen)

    ## Balls
    balls = []
    timeball1, timeball2 = 0, 0
    balle = Images[mode + 'Balle']

    ############################
    ######## Var à Théo ########
    x, y = 585, 490
    mouv = Images[mode + 'Balle'].get_rect()
    mouv.x = 586
    mouv.y = 479

    rotation_center_body = pymunk.Body(body_type=pymunk.Body.STATIC)
    rotation_center_body.position = (305, 10)
    body = space.static_body
    body.position = (303, 10)
    largeur_trait = 1.0
    l1 = pymunk.Segment(body, (5.0, 75.0), (5.0, 515.0), largeur_trait)
    l1.elasticity = 0.1
    l2 = pymunk.Segment(body, (25.0, 534.0), (110.0, 534.0), largeur_trait)
    l2.elasticity = 0.05
    l3 = pymunk.Segment(body, (110.0, 534.0), (156.0, 550.0), largeur_trait)
    l3.elasticity = 0.05
    l4 = pymunk.Segment(body, (156.0, 550.0), (300.0, 550.0), largeur_trait)
    l4.elasticity = 0.035
    l5 = pymunk.Segment(body, (376.0, 480.0), (376.0, 67.0), largeur_trait)
    l5.elasticity = 0.1
    l6 = pymunk.Segment(body, (330.0, 67.0), (376.0, 67.0), largeur_trait)
    l6.elasticity = 3.5  # Renvoie a balle (petite étoile)
    l7 = pymunk.Segment(body, (356.0, 397), (356.0, 67), 3.0)
    l7.elasticity = 0.25
    l8 = pymunk.Segment(body, (355, 105), (375.0, 105), largeur_trait)
    l8.elasticity = 0.15
    addSegment([(5, 312), (45, 238), (45, 232), (5, 210)], body, space, largeur_trait, False)
    addSegment([(352, 395), (306, 314), (338, 275), (326, 256), (352, 208)], body, space, largeur_trait, False)
    addSegment([(27, 482), (27, 337), (72, 276), (144, 311), (144, 390), (155, 418), (155, 471), (133, 455), (133, 330),
                (48, 331), (41, 338), (41, 471), (33, 482), (27, 482)], body, space, largeur_trait, True)
    addSegment([(108, 356), (72, 356), (60, 366), (60, 464), (62, 468), (94, 499), (100, 499), (122, 487), (126, 478),
                (126, 474), (114, 461), (113, 360)], body, space, largeur_trait, True)
    l9 = pymunk.Segment(body, (174, 370), (174, 331), 4.0)
    l9.elasticity = 0.5
    addSegment([(93, 64), (93, 59), (67, 59), (59, 51), (59, 62), (41, 62), (41, 105), (34, 105), (34, 160), (39, 160),
                (39, 109), (49, 109)], body, space, largeur_trait, False)
    addSegment([(322, 146), (322, 103), (330, 94), (330, 67), (301, 67), (301, 49), (284, 66), (259, 66), (312, 96),
                (312, 146)], body, space, largeur_trait, False)
    addSegment([(95, 97), (99, 97), (102, 99), (102, 105), (80, 160), (80, 116), (77, 112), (77, 107)], body, space,
               largeur_trait, True)
    addSegment([(258, 98), (252, 103), (279, 160), (282, 160), (282, 110)], body, space, largeur_trait, True)
    addSegment([(309, 214), (317, 194), (317, 159), (315, 159), (296, 201), (295, 206), (302, 214)], body, space,
               largeur_trait, True)
    arcG((5.0, 75), (160, -5), (160, 185), body, space, largeur_trait)
    arcG((190.0, -5.0), (330.0, 67.0), (190, 173), body, space, largeur_trait)
    arcG((25, 534), (5, 515), (24.5, 514.5), body, space, largeur_trait)
    arcG((376, 480), (300, 550), (303, 477), body, space, largeur_trait)
    arcG((49, 109), (93, 64), (139, 157), body, space, largeur_trait)
    arcG((322, 146), (312, 146), (317, 146), body, space, largeur_trait)
    ## Barage_raquette ##
    # todo : Ajouter un joint pour faire s'ouvrir et se fermer les barages...
    l10 = pymunk.Segment(body, (8, 177), (33, 162), largeur_trait)  # Barage en bas à droite
    l13 = pymunk.Segment(body, (125, 479), (146, 466), largeur_trait)  # Barage chambre
    l13.elasticity = 1.75
    ## Bloqueur gauche et droit (bloc vert) ##
    l11 = pymunk.Segment(body, (80, 160), (101, 108), largeur_trait)
    l11.elasticity = 2.05
    l12 = pymunk.Segment(body, (278, 160), (252, 105), largeur_trait)
    l12.elasticity = 2.05

    l19 = pymunk.Segment(body, (204, 458), (204, 424), largeur_trait)
    l19.elasticity = 0.5
    l14 = pymunk.Segment(body, (227, 465), (227, 424), largeur_trait)
    l14.elasticity = 0.5
    l15 = pymunk.Segment(body, (248, 476), (248, 424), largeur_trait)
    l15.elasticity = 0.5
    l16 = pymunk.Segment(body, (271, 476), (271, 424), largeur_trait)
    l16.elasticity = 0.5
    l17 = pymunk.Segment(body, (298, 465), (298, 424), largeur_trait)
    l17.elasticity = 0.5
    l18 = pymunk.Segment(body, (319, 458), (319, 424), largeur_trait)
    l18.elasticity = 0.5
    ## On ajoute des segments
    space.add(l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12, l13)
    space.add(l14, l15, l16, l17, l18, l19) #Traits pour NIGHT


    # Test barage lanceur (apparait après avoir lancer la balle, disparait avant d'en lancer une nouvelle
    """## Barage lanceur ##
    body_brg_lcr = space.static_body
    body_brg_lcr.position = (123, 10)
    brg_lcr = pymunk.Segment(body_brg_lcr, (453, 390), (474, 407), 1)  # Barage lanceur
    brg_lcr.elasticity = 1.75
    space.add(brg_lcr)"""

    # joint pour le barage du lanceur
    # todo : joint pour la sortir du lanceur
    """body_joint_brg_lcr = pymunk.Body(body_type=pymunk.Body.STATIC)
    body_joint_brg_lcr.position = body_brg_lcr.position
    j_brg_lcr = pymunk.PinJoint(body_brg_lcr, body_joint_brg_lcr, (0, 0), (0, 0))
    s_brg_lcr = pymunk.DampedRotarySpring(body_brg_lcr, body_joint_brg_lcr, 0.3, 50000000, 2000000)
    space.add(j_brg_lcr, s_brg_lcr)"""

    ###############################
    ###############################



    ### Raquette gauche et droite
    fp = [(7, -7), (-55, 0), (10, 10)]
    mass = 100
    moment = pymunk.moment_for_poly(mass, fp)

    # right flip
    r_flipper_body = pymunk.Body(mass, moment)
    r_flipper_body.position = 550, 60
    r_flipper_shape = pymunk.Poly(r_flipper_body, fp)
    space.add(r_flipper_body, r_flipper_shape)

    # joint right flip
    r_flipper_joint_body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
    r_flipper_joint_body.position = r_flipper_body.position
    j_r = pymunk.PinJoint(r_flipper_body, r_flipper_joint_body, (0, 0), (0, 0))
    s_r = pymunk.DampedRotarySpring(r_flipper_body, r_flipper_joint_body, 0.34, 50000000, 2000000)
    space.add(j_r, s_r)

    # left flip
    l_flipper_body = pymunk.Body(mass, moment)
    l_flipper_body.position = 410, 60
    l_flipper_shape = pymunk.Poly(l_flipper_body, [(-x, y) for x, y in fp])
    space.add(l_flipper_body, l_flipper_shape)

    # joint left flip
    l_flipper_joint_body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
    l_flipper_joint_body.position = l_flipper_body.position
    j_l = pymunk.PinJoint(l_flipper_body, l_flipper_joint_body, (0, 0), (0, 0))
    s_l = pymunk.DampedRotarySpring(l_flipper_body, l_flipper_joint_body, -0.34, 70000000, 900000)
    space.add(j_l, s_l)

    r_flipper_shape.group = l_flipper_shape.group = 1
    r_flipper_shape.elasticity = l_flipper_shape.elasticity = 0

    ### Ajout + Physic bumpers

    for p in [(506, 400), (623, 401), (559, 283)]:
        body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
        body.position = p
        shape = pymunk.Circle(body, 11)
        shape.elasticity = 2
        space.add(shape)
    for p in [(487, 283), (558, 353)]:
        body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
        body.position = p
        shape = pymunk.Circle(body, 14)
        shape.elasticity = 2
        space.add(shape)

    # Position initiale des raquettes
    left_x, left_y = 96, 295
    right_x, right_y = 235, 294

    # Est-ce que la balle est lancé ?
    ball_lancer = 0  # 0 = non / 1 = oui

    running = True

    # Menu a afficher
    menu = 0

    clock = pygame.time.Clock()

    while running:
        playMusic(menu, mode)

        if menu == 0:
            screen.blit(Images['MenuBackground'], (0, 0))
            if 15 <= pygame.mouse.get_pos()[0] <= 185 and 460 <= pygame.mouse.get_pos()[1] <= 516:
                screen.blit(Images['MenuKawaiO'], (10, 460))
            else:
                screen.blit(Images['MenuKawai'], (10, 460))
            if creepydeblock == 0:
                screen.blit(Images['MenuCreepyV'], (15, 520))
            else:
                if 15 <= pygame.mouse.get_pos()[0] <= 185 and 520 <= pygame.mouse.get_pos()[1] <= 576:
                    screen.blit(Images['MenuCreepyO'], (15, 520))
                else:
                    screen.blit(Images['MenuCreepy'], (15, 520))

        if menu == 1:
            screen.blit(Images[mode + 'Background'], (0, 0))
            space.debug_draw(draw_options)

            screen.blit(balle, (body.position.x - 5, 595 - body.position.y))

            if 65 <= pygame.mouse.get_pos()[0] <= 245 and 90 <= pygame.mouse.get_pos()[1] <= 146:
                screen.blit(Images[mode + 'BMenuO'], (60, 90))
            else:
                screen.blit(Images[mode + 'BMenu'], (60, 90))
            if 65 <= pygame.mouse.get_pos()[0] <= 245 and 160 <= pygame.mouse.get_pos()[1] <= 216:
                screen.blit(Images[mode + 'BAideO'], (60, 160))
            else:
                screen.blit(Images[mode + 'BAide'], (60, 160))
            if 65 <= pygame.mouse.get_pos()[0] <= 245 and 230 <= pygame.mouse.get_pos()[1] <= 286:
                screen.blit(Images[mode + 'BQuitterO'], (60, 230))
            else:
                screen.blit(Images[mode + 'BQuitter'], (60, 230))
            if 740 <= pygame.mouse.get_pos()[0] <= 812 and 510 <= pygame.mouse.get_pos()[1] <= 582:
                screen.blit(Images[mode + 'BRestartO'], (740, 510))
            else:
                screen.blit(Images[mode + 'BRestart'], (740, 510))
            if 880 <= pygame.mouse.get_pos()[0] <= 952 and 510 <= pygame.mouse.get_pos()[1] <= 582:
                screen.blit(Images[mode + 'BPauseO'], (880, 510))
            else:
                screen.blit(Images[mode + 'BPause'], (880, 510))

            ## Flips Gauche et droit ##
            screen.blit(Images[mode + 'left'], (left_x, left_y))
            screen.blit(Images[mode + 'right'], (right_x, right_y))

            r_flipper_body.position = 550, 69
            l_flipper_body.position = 410, 69
            r_flipper_body.velocity = l_flipper_body.velocity = 0, 0

        if menu == 2:
            screen.blit(Images[mode + 'Win'], (0, 0))

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                running = False
            if event.type == KEYDOWN and event.key == K_p:
                now = datetime.datetime.now()
                date = str(now.year) + str(now.month) + str(now.day) + str(now.hour) + str(now.minute) + str(now.second)
                print(date)
                pygame.image.save(screen, "screenshots/screenshot" + date + ".png")

            if menu == 0:
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if 15 <= pygame.mouse.get_pos()[0] <= 185 and 460 <= pygame.mouse.get_pos()[1] <= 516:
                        mode = 'Kawai'
                        menu = 1
                    elif 15 <= pygame.mouse.get_pos()[0] <= 185 and 520 <= pygame.mouse.get_pos()[1] <= 576 and creepydeblock == 1:
                        mode = 'Creepy'
                        menu = 1

            if menu == 1:

                # Clic
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if 65 <= pygame.mouse.get_pos()[0] <= 245 and 90 <= pygame.mouse.get_pos()[1] <= 146:
                        print('Menu')

                    if 65 <= pygame.mouse.get_pos()[0] <= 245 and 160 <= pygame.mouse.get_pos()[1] <= 216:
                        print('Aide')

                    if 65 <= pygame.mouse.get_pos()[0] <= 245 and 230 <= pygame.mouse.get_pos()[1] <= 286:
                       print('Quitter')

                    if 740 <= pygame.mouse.get_pos()[0] <= 812 and 510 <= pygame.mouse.get_pos()[1] <= 582:
                        print('Restart')

                    if 880 <= pygame.mouse.get_pos()[0] <= 952 and 510 <= pygame.mouse.get_pos()[1] <= 582:
                        pause = False if pause else True

                # Raquettes gauche(f) et droite(j)

                # Raquettes levé
                if event.type == KEYDOWN and event.key == K_j:
                    # Mouvement raquette
                    space.remove(j_r, s_r)
                    s_r = pymunk.DampedRotarySpring(r_flipper_body, r_flipper_joint_body, -0.4, 70000000, 1300000)
                    s_r.angular_velocity = 10000
                    space.add(j_r, s_r)

                    right_x, right_y = 137, 197

                if event.type == KEYDOWN and event.key == K_f:
                    # Mouvement raquette
                    space.remove(j_l, s_l)
                    s_l = pymunk.DampedRotarySpring(l_flipper_body, l_flipper_joint_body, 0.4, 70000000, 1300000)
                    s_l.angular_velocity = 10000
                    space.add(j_l, s_l)

                    left_x, left_y = -2, 198

                    # Raquettes baissé
                if event.type == KEYUP and event.key == K_j:
                    # Mouvement raquette
                    space.remove(j_r, s_r)
                    s_r = pymunk.DampedRotarySpring(r_flipper_body, r_flipper_joint_body, 0.34, 70000000, 1300000)
                    space.add(j_r, s_r)

                    right_x, right_y = 235, 294

                if event.type == KEYUP and event.key == K_f:
                    # Mouvement raquette
                    space.remove(j_l, s_l)
                    s_l = pymunk.DampedRotarySpring(l_flipper_body, l_flipper_joint_body, -0.34, 70000000, 1300000)
                    space.add(j_l, s_l)

                    left_x, left_y = 96, 295

                # Tilt gauche(d) et droit(k) / Non fonctionnel
                # todo : rendre le tilt fonctionnel
                # Si le joueur tilt 3 fois de suite, il perd sa balle...
                if event.type == KEYDOWN and event.key == K_d:
                    body.position.y = body.position.y + 30

                if event.type == KEYDOWN and event.key == K_k:
                    body.position.y = body.position.y - 30


                    # Balle en jeu
                if event.type == KEYDOWN and event.key == K_b:
                    mass = 1
                    radius = 5
                    ball_lancer = 0
                    inertia = pymunk.moment_for_circle(mass, 0, radius, (0, 0))
                    body = pymunk.Body(mass, inertia)
                    body.position = 670, 125  # Normale
                    shape = pymunk.Circle(body, radius, (0, 0))
                    shape.elasticity = 0.95
                    space.add(body, shape)
                    balls.append(shape)



                ##### Partie Lanceur #####
                timeball = pygame.time.get_ticks()

                if event.type == KEYDOWN and event.key == K_SPACE:
                    # space.remove(brg_lcr)
                    pygame.key.set_repeat(1, 1000)
                    y += 10
                    timeball1 = timeball

                if event.type == KEYUP and event.key == K_SPACE:
                    y = 490
                    timeball2 = timeball
                    energyball = ((timeball2 - timeball1) + 500) * 320 / 200
                    if energyball > 3000 and ball_lancer == 0:
                        energyball = random.randint(2800, 3200)
                        body.apply_impulse_at_local_point(Vec2d.unit() * energyball, (-100, 0))
                        ball_lancer = 1
                    elif energyball <= 3000 and ball_lancer == 0:
                        body.apply_impulse_at_local_point(Vec2d.unit() * energyball, (-100, 0))
                        ball_lancer = 1

        ###########################


        ### Remove any balls outside
        to_remove = []
        for ball in balls:
            if ball.body.position.get_distance((300, 300)) > 1000:
                to_remove.append(ball)

        for ball in to_remove:
            space.remove(ball.body, ball)
            balls.remove(ball)
            ball_lancer = 0

        ### Update physics
        if not pause:
            dt = 1.0 / 60.0 / 5.
            for x in range(5):
                space.step(dt)

        ### Flip screen
        pygame.display.flip()
        clock.tick(50)

parse(screen)
pygame.quit()
