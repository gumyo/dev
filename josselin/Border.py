#!/usr/bin/env python3.6m
import sys, random
import pygame
from pygame.locals import *
import pymunk
import pymunk.pygame_util
from math import sqrt
from math import cos
from math import sin
from math import asin


def arcG(A, B, C, body, space, largeur_trait):
    R = sqrt((C[0] - A[0]) ** 2 + (C[1] - A[1]) ** 2)
    coeff = round(sqrt((B[0] - A[0]) ** 2 + (B[1] - A[1]) ** 2)) + 3
    AB = [B[0] - A[0], B[1] - A[1]]
    CA = [A[0] - C[0], A[1] - C[1]]
    alpha = asin(sqrt(AB[0] ** 2 + AB[1] ** 2) / (2 * R)) / 3.14159265 * 360  # calcul de l'angle
    omega = alpha / coeff
    Cord1 = [C[0] + sin(omega / 2262) * R * (-1 if CA[0] < 0 else 1), C[1] + cos(omega / 2262) * R * (-1 if CA[1] < 0 else 1)]

    lCord = []
    lCord.append(A if (Cord1[0] - A[0]) ** 2 + (Cord1[1] - A[1]) ** 2 < (Cord1[0] - B[0]) ** 2 + (Cord1[1] - B[1]) ** 2 else B)

    for i in range(1, coeff):
        cordx = C[0] + sin(omega * i / 360 * 2 * 3.14159265) * R * (-1 if CA[0] < 0 else 1)
        cordy = C[1] + cos(omega * i / 360 * 2 * 3.14159265) * R * (-1 if CA[1] < 0 else 1)
        lCord.append([cordx, cordy])

    lCord.append(B if (Cord1[0] - A[0]) ** 2 + (Cord1[1] - A[1]) ** 2 < (Cord1[0] - B[0]) ** 2 + (Cord1[1] - B[1]) ** 2 else A)

    for i in range(0, len(lCord) - 1):
        space.add(pymunk.Segment(body, lCord[i], lCord[i+1], largeur_trait))


def add_lines(space):
    rotation_center_body = pymunk.Body(body_type = pymunk.Body.STATIC)
    rotation_center_body.position = (10, 10)

    body = pymunk.Body(10, 100000)
    body.position = (10, 10)
    largeur_trait = 1.0
    l1 = pymunk.Segment(body, (5.0, 75.0), (5.0, 515.0), largeur_trait)
    l2 = pymunk.Segment(body, (25.0, 534.0), (110.0, 534.0), largeur_trait)
    l3 = pymunk.Segment(body, (110.0, 534.0), (156.0, 550.0), largeur_trait)
    l4 = pymunk.Segment(body, (156.0, 550.0), (300.0, 550.0), largeur_trait)
    l5 = pymunk.Segment(body, (376.0, 480.0), (376.0, 67.0), largeur_trait)
    l6 = pymunk.Segment(body, (333.0, 67.0), (376.0, 67.0), largeur_trait)

    arcG((5.0, 75), (160, -5), (160, 185), body, space, largeur_trait)
    arcG((190.0, -5.0), (333.0, 67.0), (190, 173), body, space, largeur_trait)
    arcG((5, 515), (25, 534), (24.5, 514.5), body, space, largeur_trait)
    arcG((376, 480), (300, 550), (303, 477), body, space, largeur_trait)

    rotation_center_joint = pymunk.PinJoint(body, rotation_center_body, (0, 0), (0, 0))
    rotation_center_joint2 = pymunk.PinJoint(body, rotation_center_body, (390, 0), (390, 0))

    space.add(l1, l2, l3, l4, l5, l6, body, rotation_center_joint, rotation_center_joint2)

def main():
    pygame.init()
    fenetre = pygame.display.set_mode((800,600), RESIZABLE)
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

        fenetre.fill((255,255,255))

        space.debug_draw(draw_options)

        space.step(1/50.0)

        pygame.display.flip()
        clock.tick(40)

main()