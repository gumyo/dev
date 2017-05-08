#!/usr/bin/env python3.5
import sys, random
import pygame
from pygame.locals import *
import pymunk
import pymunk.pygame_util
from math import sqrt
from math import cos
from math import sin
from math import acos
from math import pi


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
        space.add(pymunk.Segment(body, liste[i - 1], liste[i], largeur_trait))
    if bol == True:
        print('test')
        space.add(pymunk.Segment(body, liste[len(liste) - 1], liste[0], largeur_trait))


def add_lines(space):
    rotation_center_body = pymunk.Body(body_type=pymunk.Body.STATIC)
    rotation_center_body.position = (223, 10)

    body = pymunk.Body(100000, 100000)
    body.position = (223, 10)
    largeur_trait = 1.0
    l1 = pymunk.Segment(body, (5.0, 75.0), (5.0, 515.0), largeur_trait)
    l2 = pymunk.Segment(body, (25.0, 534.0), (110.0, 534.0), largeur_trait)
    l3 = pymunk.Segment(body, (110.0, 534.0), (156.0, 550.0), largeur_trait)
    l4 = pymunk.Segment(body, (156.0, 550.0), (300.0, 550.0), largeur_trait)
    l5 = pymunk.Segment(body, (376.0, 480.0), (376.0, 67.0), largeur_trait)
    l6 = pymunk.Segment(body, (330.0, 67.0), (376.0, 67.0), largeur_trait)
    l7 = pymunk.Segment(body, (354.0, 400), (354.0, 67), 2.0)
    l8 = pymunk.Segment(body, (355, 105), (375.0, 105), largeur_trait)
    addSegment([(5, 312), (45, 238), (45, 232), (5, 210)], body, space, largeur_trait, False)
    addSegment([(352, 395), (306, 314), (338, 275), (326, 256), (352, 208)], body, space, largeur_trait, False)
    addSegment([(27, 482), (27, 337), (72, 276), (144, 311), (144, 390), (155, 418), (155, 471), (133, 455), (133, 331), (48, 331), (41, 338), (41, 471), (33, 482), (27, 482)], body, space, largeur_trait, True)
    addSegment([(108, 356), (72, 356), (60, 366), (60, 464), (62, 468), (94, 499), (100, 499), (122, 487), (126, 478), (126, 474), (114, 461), (113, 360)], body, space, largeur_trait, True)
    l9 = pymunk.Segment(body, (174, 370), (174, 331), 4.0) #******#
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

    centreRotation = pymunk.PinJoint(body, rotation_center_body, (0, 0), (0, 0))
    centreRotation2 = pymunk.PinJoint(body, rotation_center_body, (390, 0), (390, 0))
    centreRotation3 = pymunk.PinJoint(body, rotation_center_body, (0, 580), (0, 580))
    centreRotation4 = pymunk.PinJoint(body, rotation_center_body, (390, 580), (390, 580))

    space.add(body, centreRotation, centreRotation2, centreRotation3, centreRotation4)
    space.add(l1, l2, l3, l4, l5, l6, l7, l8, l9)


def main():
    pygame.init()
    fenetre = pygame.display.set_mode((800, 600), RESIZABLE)
    pygame.display.set_caption("Border")
    clock = pygame.time.Clock()

    space = pymunk.Space()
    space.gravity = (0.0, -900.0)

    add_lines(space)


    draw_options = pymunk.pygame_util.DrawOptions(fenetre)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                sys.exit(0)

        fenetre.fill((255, 255, 255))

        space.debug_draw(draw_options)

        space.step(1 / 50.0)

        pygame.display.flip()
        clock.tick(40)


main()
