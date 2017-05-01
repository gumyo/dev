#!/usr/bin/env python3.5
import sys, random
import pygame
from pygame.locals import *
import pymunk
import pymunk.pygame_util

def add_arc5(cord1, cord2, cord3, cord4, cord5, cord6, space, body, largeur_trait):
    l1 = pymunk.Segment(body, cord1, cord2, largeur_trait)
    l2 = pymunk.Segment(body, cord2,  cord3, largeur_trait)
    l3 = pymunk.Segment(body, cord3, cord4, largeur_trait)
    l4 = pymunk.Segment(body, cord4, cord5, largeur_trait)
    l5 = pymunk.Segment(body, cord5, cord6, largeur_trait)

    space.add(l1, l2, l3, l4, l5)

def add_arc9(cord1, cord2, cord3, cord4, cord5, cord6, cord7, cord8, cord9, cord10, space, body, largeur_trait):
    l1 = pymunk.Segment(body, cord1, cord2, largeur_trait)
    l2 = pymunk.Segment(body, cord2,  cord3, largeur_trait)
    l3 = pymunk.Segment(body, cord3, cord4, largeur_trait)
    l4 = pymunk.Segment(body, cord4, cord5, largeur_trait)
    l5 = pymunk.Segment(body, cord5, cord6, largeur_trait)
    l6 = pymunk.Segment(body, cord6, cord7, largeur_trait)
    l7 = pymunk.Segment(body, cord7, cord8, largeur_trait)
    l8 = pymunk.Segment(body, cord8, cord9, largeur_trait)
    l9 = pymunk.Segment(body, cord9, cord10, largeur_trait)

    space.add(l1, l2, l3, l4, l5, l6, l7, l8, l9)

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

    add_arc5((5.0, 75.0), (29.0, 47.3), (58.3, 24.5), (91.1, 8.9), (126.6, -2.1), (160.0, -5.0), space, body, largeur_trait)
    add_arc5((190.0, -5.0), (222.2, -1.6), (254.5, 7.1), (284.6, 22.2), (311.2, 42.7), (333.0, 67.0), space, body,largeur_trait)
    add_arc9((376.0, 480.0), (374.4, 492.6), (370.6, 504.8), (364.8, 516.1), (357.0, 526.2), (347.6, 534.8), (336.9, 541.7), (325.1, 546.6), (312.7, 549.4), (300.0, 550.0), space, body,largeur_trait)
    add_arc9((5.0, 515.0), (5.4, 518.4), (6.35, 521.64), (7.9, 524.7), (9.9, 527.4), (12.35, 529.75), (15.2, 531.65), (18.3, 533), (21.5, 533.8), (25.0, 534.0), space, body, largeur_trait)

    rotation_center_joint = pymunk.PinJoint(body, rotation_center_body, (0, 0), (0, 0))
    rotation_center_joint2 = pymunk.PinJoint(body, rotation_center_body, (390, 0), (390, 0))

    space.add(l1, l2, l3, l4, l5, l6, body, rotation_center_joint, rotation_center_joint2)

def main():
    pygame.init()
    fenetre = pygame.display.set_mode((800,600), RESIZABLE)
    pygame.display.set_caption("Joints. Just wait and the L will tip over")
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