import pygame

memory = [0]*4096
register = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 0xA: 0, 0xB: 0, 0xC: 0, 0xD: 0, 0xE: 0, 0xF: 0}
# La chip 8 possède 16 registers de 8 bits de V0 à VF
stack = [0]*16
# Stock  les adresses de retour lorsque les sous-programmes sont appelés
pointPile = 512
pointStack = 0
regI = 0
delay = 0
sound = 0
clavier = 
{
    0x0: pygame.K_0,
    0x1: pygame.K_1,
    0x2: pygame.K_2,
    0x3: pygame.K_3,
    0x4: pygame.K_4,
    0x5: pygame.K_5,
    0x6: pygame.K_6,
    0x7: pygame.K_7,
    0x8: pygame.K_8,
    0x9: pygame.K_9,
    0xA: pygame.K_a,
    0xB: pygame.K_b,
    0xC: pygame.K_c,
    0xD: pygame.K_d,
    0xE: pygame.K_e,
    0xF: pygame.K_f,
}