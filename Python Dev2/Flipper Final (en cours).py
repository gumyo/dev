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
from math import asin
from math import acos
from math import pi
from random import randint

import pygame
from pygame.locals import *
from pygame.color import *

import pymunk
from pymunk import Vec2d
import pymunk.pygame_util

# Initialisation de la fenêtre de jeu
pygame.init()
screen = pygame.display.set_mode((1000, 600))
clock = pygame.time.Clock()
running = True

# Variable du score actuel
CurrentScore = 0

# Menu a afficher
menu = 1

#####################
##### Important #####

## Arrière-plan
fond = pygame.image.load("images/fond.jpg").convert()
fond1 = pygame.image.load("images/backround.png").convert()
contour = pygame.image.load("images/contour.png").convert_alpha()

fond_kawai = pygame.image.load("Kawai/FlipperKawai.jpg")

### Physics stuff
space = pymunk.Space()
space.gravity = (0.0, -480.0)
draw_options = pymunk.pygame_util.DrawOptions(screen)


##################
##### Divers #####

## Balls
balls = []
timeball1, timeball2 = 0, 0
balle = pygame.image.load("images/balle.png").convert_alpha()

## Couloirs
rampe = pygame.image.load("images/rampe.png").convert_alpha()
couloir = pygame.image.load("images/FondCOULOIR.png").convert_alpha()
poussoir = pygame.image.load("images/Poussoir.png").convert_alpha()
cache = pygame.image.load("images/CacheDuPOUSSOIR.png").convert_alpha()

## Flippers
left = pygame.image.load("images/left.png").convert_alpha()
right = pygame.image.load("images/right.png").convert_alpha()
leftTest = pygame.image.load("images/left.png").convert_alpha()
rightTest = pygame.image.load("images/right.png").convert_alpha()

### Bumpers
bumper_un = pygame.image.load("images/Bumper_un.png").convert_alpha()
bumper_deux = pygame.image.load("images/Bumper_deux.png").convert_alpha()
bumper_trois = pygame.image.load("images/Bumper_trois_central.png").convert_alpha()
bumper_quatre = pygame.image.load("images/Bumper_quatre_gros.png").convert_alpha()
bumper_cinq = pygame.image.load("images/Bumper_cinq.png").convert_alpha()

### Obstacles
obstacle_right = pygame.image.load("images/obstacleRigth.png").convert_alpha()
obstacle_left = pygame.image.load("images/obstacleLeft.png").convert_alpha()
Cchambre = pygame.image.load("images/ContourChambre.png").convert_alpha()
Echambre = pygame.image.load("images/interieurChambre.png").convert_alpha()
Barage_chambre = pygame.image.load("images/Barage_raquette.png").convert_alpha()
FuturGIF_chambre = pygame.image.load("images/FuturGIF_chambre.png").convert_alpha()
FuturGIF_chambre2 = pygame.image.load("images/FuturGIF_chambre.png").convert_alpha()
Item_raquette_droite = pygame.image.load("images/Item_raquette_droite.png").convert_alpha()
Item_raquette_gauche = pygame.image.load("images/Item_raquette_gauche.png").convert_alpha()
Top_droite = pygame.image.load("images/Top_A_Droite.png").convert_alpha()
Bloqueur_droit = pygame.image.load("images/bloqueurDroit.png").convert_alpha()
Bloqueur_gauche = pygame.image.load("images/bloqueurGauche.png").convert_alpha()

### Star
star = pygame.image.load("images/star.png").convert_alpha()
star_socle = pygame.image.load("images/StarSOCLE.png").convert_alpha()
petitbarrage = pygame.image.load("images/petitBarage.png").convert_alpha()


##################
##### Lettre #####

### ABCD
pointiller_A = pygame.image.load("images/A_Trait.png").convert_alpha()
pointiller_B = pygame.image.load("images/B_Trait.png").convert_alpha()
pointiller_C = pygame.image.load("images/C_Trait.png").convert_alpha()
pointiller_D = pygame.image.load("images/D_Trait.png").convert_alpha()

### Night
N_night = pygame.image.load("images/n_night.png").convert_alpha()
I_night = pygame.image.load("images/i_night.png").convert_alpha()
G_night = pygame.image.load("images/G_night.png").convert_alpha()
H_night = pygame.image.load("images/h_night.png").convert_alpha()
T_night = pygame.image.load("images/t_night.png").convert_alpha()

### FLY
Pt_F = pygame.image.load("images/FLY_BarreF.png").convert_alpha()
Pt_L = pygame.image.load("images/FLY_BarreL.png").convert_alpha()
Pt_Y = pygame.image.load("images/FLY_BarreY.png").convert_alpha()

### Drop
D_drop = pygame.image.load("images/D_drop.png").convert_alpha()
R_drop = pygame.image.load("images/R_drop.png").convert_alpha()
O_drop = pygame.image.load("images/O_drop.png").convert_alpha()
P_drop = pygame.image.load("images/P_drop.png").convert_alpha()
Barage_raquette = pygame.image.load("images/Barage_raquette.png").convert_alpha()




############################
######## Var à Théo ########

continuer = 1
x, y = 585, 490
press = pygame.key.set_repeat(1, 1000)
mouv = balle.get_rect()
mouv.x = 586
mouv.y = 479
perm = False
collision = False
compteur = 0
temps = 0
dep = 200


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
        mouv.y +=1 * math.sin(alpha)
        mouv.x -=1 * math.cos(alpha)
    #couleur_position_balle = int('%02x%02x%02x' % (r1, g1, b1), 16)
    if perm:
        mouv.y -=1 * math.sin(alpha)
        mouv.x +=1 * math.cos(alpha)
    return mouv

############################
############################


#--------------------------#


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
        space.add(pymunk.Segment(body, (lCoords[i][0] + C[0], lCoords[i][1] + C[1]), (lCoords[i + 1][0] + C[0], lCoords[i + 1][1] + C[1]), largeur_trait))


def addSegment(liste, body, space, largeur_trait, bol):
    for i in range(1, len(liste)):
        l = pymunk.Segment(body, liste[i - 1], liste[i], largeur_trait)
        l.elasticity = 0.5
        space.add(l)
    if bol == True:
        l = pymunk.Segment(body, liste[len(liste) - 1], liste[0], largeur_trait)
        l.elasticity = 0.5
        space.add(l)


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
l6.elasticity = 3.5 # Renvoie a balle (petite étoile)
l7 = pymunk.Segment(body, (356.0, 397), (356.0, 67), 3.0)
l7.elasticity = 0.25
l8 = pymunk.Segment(body, (355, 105), (375.0, 105), largeur_trait)
l8.elasticity = 0.15
addSegment([(5, 312), (45, 238), (45, 232), (5, 210)], body, space, largeur_trait, False)
addSegment([(352, 395), (306, 314), (338, 275), (326, 256), (352, 208)], body, space, largeur_trait, False)
addSegment([(27, 482), (27, 337), (72, 276), (144, 311), (144, 390), (155, 418), (155, 471), (133, 455), (133, 330), (48, 331), (41, 338), (41, 471), (33, 482), (27, 482)], body, space, largeur_trait, True)
addSegment([(108, 356), (72, 356), (60, 366), (60, 464), (62, 468), (94, 499), (100, 499), (122, 487), (126, 478), (126, 474), (114, 461), (113, 360)], body, space, largeur_trait, True)
l9 = pymunk.Segment(body, (174, 370), (174, 331), 4.0)
l9.elasticity = 0.5
addSegment([(93, 64), (93, 59), (67, 59), (59, 51), (59, 62), (41, 62), (41, 105), (34, 105), (34, 160), (39, 160), (39, 109), (49,109)], body, space, largeur_trait, False)
addSegment([(322, 146), (322, 103), (330, 94), (330, 67), (301, 67), (301, 49), (284, 66), (259, 66), (312, 96), (312, 146)],  body, space, largeur_trait, False)
addSegment([(95, 97), (99, 97), (102,99), (102, 105), (80, 160), (80, 116), (77, 112), (77, 107)], body, space, largeur_trait, True)
addSegment([(258, 98), (252, 103), (279, 160), (282, 160), (282, 110)], body, space, largeur_trait, True)
addSegment([(309, 214), (317, 194), (317, 159), (315, 159), (296, 201), (295, 206), (302, 214)], body, space, largeur_trait, True)
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
## On ajoute des segments
space.add(l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12, l13)


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
# todo : Enlever les flips de l'écran (les cacher), ne garder que les images...

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

for p in [(475, 285), (402, 285), (421, 398)]:
    body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
    body.position = p
    shape = pymunk.Circle(body, 11)
    shape.elasticity = 1.2
    space.add(shape)
for p in [(475, 355), (543, 400)]:
    body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
    body.position = p
    shape = pymunk.Circle(body, 14)
    shape.elasticity = 1.2
    space.add(shape)


## Physics poussoir
"""
coordfrm1y = 90
def poussoir1(mass, coordfrm1y):
    for p in [(580, coordfrm1y)]:
        frm1 = [(0, 0), (0, 20), (20, 20), (20, 0)]
        mmfrm1 = pymunk.moment_for_poly(mass, frm1)
        frm1_body = pymunk.Body(mass, mmfrm1)
        frm1_body.position = p
        frm1_shape = pymunk.Poly(frm1_body, frm1)
        space.add(frm1_body, frm1_shape)
        frm1_joint_body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
        frm1_joint_body.position = frm1_body.position
        frm1_j = pymunk.PinJoint(frm1_body, frm1_joint_body, (0, 0), (0, 0))
        frm1_s = pymunk.DampedRotarySpring(frm1_body, frm1_joint_body, 0, 50000000, 2000000)
        space.add(frm1_j, frm1_s)
poussoir1(mass, coordfrm1y)"""

# Position initiale des raquettes
left_x, left_y = 96, 295
right_x, right_y = 235, 294

# Est-ce que la balle est lancé ?
ball_lancer = 0  # 0 = non / 1 = oui



while running:

### Draw stuff
    space.debug_draw(draw_options)
    pygame.draw.rect(screen, [0, 0, 0], (0, 0, 100, 600))

    if menu == 1:
        screen.blit(fond_kawai, (0, 0))
        space.debug_draw(draw_options)
        # ## Lanceur
        # screen.blit(contour, (213, 0))
        # screen.blit(couloir, (575, 177))
        # screen.blit(rampe, (575, 180))
        # screen.blit(poussoir, (585, y))
        # screen.blit(cache, (577, 523))
        #
        # ## Générale
        screen.blit(balle, (body.position.x - 5, 595 - body.position.y))
        # screen.blit(bumper_un, (460, 300))
        # screen.blit(bumper_deux, (390, 300))
        # screen.blit(bumper_trois, (460, 230))
        # screen.blit(bumper_quatre, (527, 185))
        # screen.blit(bumper_cinq, (410, 190))
        # screen.blit(obstacle_right, (528, 196))
        # screen.blit(obstacle_left, (228, 278))
        # screen.blit(Cchambre, (248, 89))
        # screen.blit(Echambre, (282, 90))
        # screen.blit(Barage_chambre, (342, 103))
        # screen.blit(FuturGIF_chambre, (258, 175))
        # screen.blit(FuturGIF_chambre2, (368, 224))
        # screen.blit(Item_raquette_droite, (483, 440))
        # screen.blit(Item_raquette_gauche, (256, 426))
        # screen.blit(Top_droite, (514, 372))
        # screen.blit(Bloqueur_droit, (474, 430))
        # screen.blit(Bloqueur_gauche, (297, 428))
        # screen.blit(petitbarrage, (393, 215))
        # screen.blit(star, (555, 499))
        # screen.blit(star_socle, (555, 523))
        #
        # ## Texte ##
        # screen.blit(pointiller_A, (525, 281))
        # screen.blit(pointiller_B, (541, 297))
        # screen.blit(pointiller_C, (324, 85))
        # screen.blit(pointiller_D, (342, 96))
        #
        # screen.blit(N_night, (420, 150))
        # screen.blit(I_night, (450, 150))
        # screen.blit(G_night, (473, 150))
        # screen.blit(H_night, (502, 150))
        # screen.blit(T_night, (530, 150))
        #
        # screen.blit(Pt_F, (300, 308))
        # screen.blit(Pt_L, (325, 298))
        # screen.blit(Pt_Y, (350, 286))
        #
        # screen.blit(D_drop, (246, 431))
        # screen.blit(R_drop, (266, 431))
        # screen.blit(O_drop, (280, 431))
        # screen.blit(P_drop, (292, 431))
        # screen.blit(Barage_raquette, (230, 408))
        #
        ## Flips Gauche et droit ##
        screen.blit(left, (left_x, left_y))
        screen.blit(right, (right_x, right_y))

        r_flipper_body.position = 550, 69
        l_flipper_body.position = 410, 69
        r_flipper_body.velocity = l_flipper_body.velocity = 0, 0

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            running = False
        if event.type == KEYDOWN and event.key == K_p:
            pygame.image.save(screen, "flipper.png")

        if menu == 1:
            # Raquettes gauche(f) et groite(j)

        # Raquettes levé
            if event.type == KEYDOWN and event.key == K_j:
                # Mouvement raquette
                space.remove(j_r, s_r)
                s_r = pymunk.DampedRotarySpring(r_flipper_body, r_flipper_joint_body, -0.4, 70000000, 1300000)
                s_r.angular_velocity = 10000
                space.add(j_r, s_r)
                # Position image
                right = pygame.transform.rotate(rightTest, -43)
                right_x, right_y = 137, 197

            if event.type == KEYDOWN and event.key == K_f:
                # Mouvement raquette
                space.remove(j_l, s_l)
                s_l = pymunk.DampedRotarySpring(l_flipper_body, l_flipper_joint_body, 0.4, 70000000, 1300000)
                s_l.angular_velocity = 10000
                space.add(j_l, s_l)
                # Position image
                left = pygame.transform.rotate(leftTest, 42)
                left_x, left_y = -2, 198

        # Raquettes baissé
            if event.type == KEYUP and event.key == K_j:
                # Mouvement raquette
                space.remove(j_r, s_r)
                s_r = pymunk.DampedRotarySpring(r_flipper_body, r_flipper_joint_body, 0.34, 70000000, 1300000)
                space.add(j_r, s_r)
                # Position image
                right = pygame.transform.rotate(rightTest, 0)
                right_x, right_y = 235, 294

            if event.type == KEYUP and event.key == K_f:
                # Mouvement raquette
                space.remove(j_l, s_l)
                s_l = pymunk.DampedRotarySpring(l_flipper_body, l_flipper_joint_body, -0.34, 70000000, 1300000)
                space.add(j_l, s_l)
                # Position image
                left = pygame.transform.rotate(leftTest, -0)
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
                radius = 4
                ball_lancer = 0
                inertia = pymunk.moment_for_circle(mass, 0, radius, (0, 0))
                body = pymunk.Body(mass, inertia)
                body.position = 670, 125  # Normale
                #body.position = 480, 228  # test
                shape = pymunk.Circle(body, radius, (0, 0))
                shape.elasticity = 0.95
                space.add(body, shape)
                balls.append(shape)



    ##### Partie Lanceur #####
            timeball = pygame.time.get_ticks()

            if event.type == KEYDOWN and event.key == K_SPACE:
                #space.remove(brg_lcr)
                pygame.key.set_repeat(1, 1000)
                perm = False
                y += 10
                Ppoussoir = (x, y)
                timeball1 = timeball

            if event.type == KEYUP and event.key == K_SPACE:
                perm = True
                y = 490
                Ppoussoir = (x, y)
                timeball2 = timeball
                energyball = ((timeball2 - timeball1) + 500)*320 / 200
                if energyball > 3000 and ball_lancer == 0:
                    energyball = random.randint(2800, 3200)
                    body.apply_impulse_at_local_point(Vec2d.unit() * energyball, (-100, 0))
                    #body.angular_velocity = 1
                    ball_lancer = 1
                elif energyball <= 3000 and ball_lancer == 0:
                    body.apply_impulse_at_local_point(Vec2d.unit() * energyball, (-100, 0))
                    #body.angular_velocity = 1
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
    dt = 1.0 / 60.0 / 5.
    for x in range(5):
        space.step(dt)

    ### Flip screen
    pygame.display.flip()
    clock.tick(50)
    pygame.display.set_caption("FPS : " + str(round(clock.get_fps(), 1)))
