"""A very basic flipper game."""
__version__ = "$Id:$"
__docformat__ = "reStructuredText"

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

import pygame
from pygame.locals import *
from pygame.color import *

import pymunk
from pymunk import Vec2d
import pymunk.pygame_util

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True


## Arrière-plan
fond = pygame.image.load("images/fond.jpg").convert()
fond1 = pygame.image.load("images/backround.png").convert()
contour = pygame.image.load("images/contour.png").convert_alpha()


### Physics stuff
space = pymunk.Space()
space.gravity = (0.0, -900.0)
draw_options = pymunk.pygame_util.DrawOptions(screen)

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


### Bumpers
bumper_un = pygame.image.load("images/Bumper_un.png").convert_alpha()
bumper_deux = pygame.image.load("images/Bumper_deux.png").convert_alpha()
bumper_trois = pygame.image.load("images/Bumper_trois_central.png").convert_alpha()
bumper_quatre = pygame.image.load("images/Bumper_quatre_gros.png").convert_alpha()
bumper_cinq = pygame.image.load("images/Bumper_cinq.png").convert_alpha()


### Obstacles
obstacle_right = pygame.image.load("images/obstacleRigth.png").convert_alpha()
obstacle_left = pygame.image.load("images/obstacleLeft.png").convert_alpha()



############################
##### Var à Théo #####
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



############################
##### Contour josselin #####


def arcG(A, B, C, body, space, largeur_trait):
    R = sqrt((C[0] - A[0]) ** 2 + (C[1] - A[1]) ** 2)
    coeff = round(sqrt((B[0] - A[0]) ** 2 + (B[1] - A[1]) ** 2)) + 3
    AB = [B[0] - A[0], B[1] - A[1]]
    CA = [A[0] - C[0], A[1] - C[1]]
    alpha = asin(sqrt(AB[0] ** 2 + AB[1] ** 2) / (2 * R)) * 2  # calcul de l'angle
    omega = alpha / coeff
    betaH = pi - acos(CA[0] / R)
    gammaV = pi - acos(CA[1] / R)
    Cord1 = [C[0] + sin(omega) * R * (-1 if CA[0] < 0 else 1), C[1] + cos(omega) * R * (-1 if CA[1] < 0 else 1)]
    print(betaH, gammaV)

    lCord = []
    lCord.append(
        A if (Cord1[0] - A[0]) ** 2 + (Cord1[1] - A[1]) ** 2 < (Cord1[0] - B[0]) ** 2 + (Cord1[1] - B[1]) ** 2 else B)

    for i in range(1, coeff):
        cordx = C[0] + sin(omega * i) * R * (-1 if CA[0] < 0 else 1)
        cordy = C[1] + cos(omega * i) * R * (-1 if CA[1] < 0 else 1)
        lCord.append([cordx, cordy])

    lCord.append(
        B if (Cord1[0] - A[0]) ** 2 + (Cord1[1] - A[1]) ** 2 < (Cord1[0] - B[0]) ** 2 + (Cord1[1] - B[1]) ** 2 else A)

    for i in range(0, len(lCord) - 1):
        space.add(pymunk.Segment(body, lCord[i], lCord[i + 1], largeur_trait))


def add_lines(space):
    rotation_center_body = pymunk.Body(body_type=pymunk.Body.STATIC)
    rotation_center_body.position = (223, 10)

    body = pymunk.Body(10, 100000)
    body.position = (223, 10)
    largeur_trait = 1.0
    l1 = pymunk.Segment(body, (5.0, 75.0), (5.0, 515.0), largeur_trait)
    l2 = pymunk.Segment(body, (25.0, 534.0), (110.0, 534.0), largeur_trait)
    l3 = pymunk.Segment(body, (110.0, 534.0), (156.0, 550.0), largeur_trait)
    l4 = pymunk.Segment(body, (156.0, 550.0), (300.0, 550.0), largeur_trait)
    l5 = pymunk.Segment(body, (376.0, 480.0), (376.0, 67.0), largeur_trait)
    l6 = pymunk.Segment(body, (333.0, 67.0), (376.0, 67.0), largeur_trait)
    l7 = pymunk.Segment(body, (353.0, 400), (353.0, 67), 3.0)
    l8 = pymunk.Segment(body, (355, 100), (375.0, 100), largeur_trait)
    l9 = pymunk.Segment(body, (5, 312), (45, 238), largeur_trait)
    l10 = pymunk.Segment(body, (45, 238), (45, 232), largeur_trait)
    l11 = pymunk.Segment(body, (45, 232), (5, 210), largeur_trait)
    l12 = pymunk.Segment(body, (352, 395), (306, 314), largeur_trait)
    l13 = pymunk.Segment(body, (306, 314), (338, 275), largeur_trait)
    l14 = pymunk.Segment(body, (338, 275), (326, 256), largeur_trait)
    l15 = pymunk.Segment(body, (326, 256), (352, 208), largeur_trait)

    arcG((5.0, 75), (160, -5), (160, 185), body, space, largeur_trait)
    arcG((190.0, -5.0), (333.0, 67.0), (190, 173), body, space, largeur_trait)
    arcG((5, 515), (25, 534), (24.5, 514.5), body, space, largeur_trait)
    arcG((376, 480), (300, 550), (303, 477), body, space, largeur_trait)
    #arcG((48, 108), (94, 64), (139, 157), body, space, largeur_trait)

    centreRotation = pymunk.PinJoint(body, rotation_center_body, (0, 0), (0, 0))
    centreRotation2 = pymunk.PinJoint(body, rotation_center_body, (390, 0), (390, 0))
    centreRotation3 = pymunk.PinJoint(body, rotation_center_body, (0, 580), (0, 580))
    centreRotation4 = pymunk.PinJoint(body, rotation_center_body, (390, 580), (390, 580))

    space.add(l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12, l13, l14, l15, body, centreRotation, centreRotation2,centreRotation3, centreRotation4)


add_lines(space)

###############################
###############################



### walls
static_lines = [pymunk.Segment(space.static_body, (612, 0), (612, 600), 1)
    , pymunk.Segment(space.static_body, (212, 0), (212, 600), 1)
    , pymunk.Segment(space.static_body, (212, 600), (612, 600), 1)
                ]
for line in static_lines:
    line.elasticity = 0.7
    line.group = 1
space.add(static_lines)

fp = [(7, -7), (-55, 0), (7, 7)]
mass = 100
moment = pymunk.moment_for_poly(mass, fp)

# right flipper
r_flipper_body = pymunk.Body(mass, moment)
r_flipper_body.position = 470, 69
r_flipper_shape = pymunk.Poly(r_flipper_body, fp)
space.add(r_flipper_body, r_flipper_shape)

r_flipper_joint_body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
r_flipper_joint_body.position = r_flipper_body.position
j = pymunk.PinJoint(r_flipper_body, r_flipper_joint_body, (0, 0), (0, 0))
# todo: tweak values of spring better
s = pymunk.DampedRotarySpring(r_flipper_body, r_flipper_joint_body, 0.61, 50000000, 2000000)
space.add(j, s)

# left flipper
l_flipper_body = pymunk.Body(mass, moment)
l_flipper_body.position = 333, 69
l_flipper_shape = pymunk.Poly(l_flipper_body, [(-x, y) for x, y in fp])
space.add(l_flipper_body, l_flipper_shape)

l_flipper_joint_body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
l_flipper_joint_body.position = l_flipper_body.position
j = pymunk.PinJoint(l_flipper_body, l_flipper_joint_body, (0, 0), (0, 0))
s = pymunk.DampedRotarySpring(l_flipper_body, l_flipper_joint_body, -0.61, 50000000, 2000000)
space.add(j, s)

r_flipper_shape.group = l_flipper_shape.group = 1
r_flipper_shape.elasticity = l_flipper_shape.elasticity = 0


## Physics bumpers
for p in [(475, 285), (402, 285), (421, 398)]:
    body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
    body.position = p
    shape = pymunk.Circle(body, 11)
    shape.elasticity = 0.75
    space.add(shape)
for p in [(475, 355), (546, 400)]:
    body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
    body.position = p
    shape = pymunk.Circle(body, 14)
    shape.elasticity = 0.75
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



while running:

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            running = False
        elif event.type == KEYDOWN and event.key == K_p:
            pygame.image.save(screen, "flipper.png")

        elif event.type == KEYDOWN and event.key == K_j:
            r_flipper_body.apply_impulse_at_local_point(Vec2d.unit() * 30000, (-100, 0))


        elif event.type == KEYDOWN and event.key == K_f:
            l_flipper_body.apply_impulse_at_local_point(Vec2d.unit() * -30000, (-100, 0))


        elif event.type == KEYDOWN and event.key == K_b:

            mass = 10
            radius = 4
            inertia = pymunk.moment_for_circle(mass, 0, radius, (0, 0))
            body = pymunk.Body(mass, inertia)
            body.position = 590, 125
            #body.position = 460, 260
            shape = pymunk.Circle(body, radius, (0, 0))
            shape.elasticity = 0.95
            space.add(body, shape)
            balls.append(shape)



############ Partie Théo ###############

        elif event.type == KEYDOWN and event.key == K_SPACE:
            pygame.key.set_repeat(1, 1000)
            perm = False
            y += 10
            Ppoussoir = (x, y)
            timeball = pygame.time.get_ticks()
            timeball1 = timeball


        elif event.type == KEYUP and event.key == K_SPACE:
            perm = True
            y = 490
            Ppoussoir = (x, y)
            timeball = pygame.time.get_ticks()
            timeball2 = timeball
            energyball = ((timeball2 - timeball1) + 2000)*4
            print("energyball", energyball)
            if energyball > 20000:
                body.apply_impulse_at_local_point(Vec2d.unit() * 20000, (-100, 0))
            else:
                body.apply_impulse_at_local_point(Vec2d.unit() * energyball, (-100, 0))


########################################



    ### Clear screen
    #screen.fill(THECOLORS["white"])
    screen.blit(fond, (0, 0))
    screen.blit(fond1, (213, 0))


    ### Draw stuff
    space.debug_draw(draw_options)

    screen.blit(contour, (213, 0))
    screen.blit(couloir, (575, 177))
    screen.blit(rampe, (575, 180))
    screen.blit(poussoir, (585, y))
    screen.blit(cache, (577, 523))

    screen.blit(balle, (body.position.x - 5, 595 - body.position.y))
    screen.blit(bumper_un, (460, 300))
    screen.blit(bumper_deux, (390, 300))
    screen.blit(bumper_trois, (460, 230))
    screen.blit(bumper_quatre, (530, 185))
    screen.blit(bumper_cinq, (410, 190))
    screen.blit(obstacle_right, (528, 196))
    screen.blit(obstacle_left, (228, 278))

    screen.blit(left, (180, 380))
    screen.blit(right, (322, 382))

    r_flipper_body.position = 470, 69
    l_flipper_body.position = 333, 69
    r_flipper_body.velocity = l_flipper_body.velocity = 0, 0


    ### Remove any balls outside
    to_remove = []
    for ball in balls:
        if ball.body.position.get_distance((300, 300)) > 1000:
            to_remove.append(ball)

    for ball in to_remove:
        space.remove(ball.body, ball)
        balls.remove(ball)


    ### Update physics
    dt = 1.0 / 60.0 / 5.
    for x in range(5):
        space.step(dt)


    ### Flip screen
    pygame.display.flip()
    clock.tick(50)
    pygame.display.set_caption("FPS : " + str(round(clock.get_fps(), 1)))
