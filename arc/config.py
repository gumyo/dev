import pygame
from pygame import key


def nombre(memory):
    memory[0], memory[1], memory[2], memory[3], memory[4] = 0xF0, 0x90, 0x90, 0x90, 0xF0  # O
    memory[5], memory[6], memory[7], memory[8], memory[9] = 0x20, 0x60, 0x20, 0x20, 0x70  # 1
    memory[10], memory[11], memory[12], memory[13], memory[14] = 0xF0, 0x10, 0xF0, 0x80, 0xF0  # 2
    memory[15], memory[16], memory[17], memory[18], memory[19] = 0xF0, 0x10, 0xF0, 0x10, 0xF0  # 3
    memory[20], memory[21], memory[22], memory[23], memory[24] = 0x90, 0x90, 0xF0, 0x10, 0x10  # 4
    memory[25], memory[26], memory[27], memory[28], memory[29] = 0xF0, 0x80, 0xF0, 0x10, 0xF0  # 5
    memory[30], memory[31], memory[32], memory[33], memory[34] = 0xF0, 0x80, 0xF0, 0x90, 0xF0  # 6
    memory[35], memory[36], memory[37], memory[38], memory[39] = 0xF0, 0x10, 0x20, 0x40, 0x40  # 7
    memory[40], memory[41], memory[42], memory[43], memory[44] = 0xF0, 0x90, 0xF0, 0x90, 0xF0  # 8
    memory[45], memory[46], memory[47], memory[48], memory[49] = 0xF0, 0x90, 0xF0, 0x10, 0xF0  # 9
    memory[50], memory[51], memory[52], memory[53], memory[54] = 0xF0, 0x90, 0xF0, 0x90, 0x90  # A
    memory[55], memory[56], memory[57], memory[58], memory[59] = 0xE0, 0x90, 0xE0, 0x90, 0xE0  # B
    memory[60], memory[61], memory[62], memory[63], memory[64] = 0xF0, 0x80, 0x80, 0x80, 0xF0  # C
    memory[65], memory[66], memory[67], memory[68], memory[69] = 0xE0, 0x90, 0x90, 0x90, 0xE0  # D
    memory[70], memory[71], memory[72], memory[73], memory[74] = 0xF0, 0x80, 0xF0, 0x80, 0xF0  # E
    memory[75], memory[76], memory[77], memory[78], memory[79] = 0xF0, 0x80, 0xF0, 0x80, 0x80  # F
    return memory


def timers(delay, sound):
    if delay != 0:
        delay -= 1
    if sound != 0:
        sound -= 1
    return delay, sound


def iniVar():
    memory = [0] * 4096
    memory = romOpen(memory)
    memory = nombre(memory)
    register = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0}
    keys = [pygame.K_u, pygame.K_h, pygame.K_k, pygame.K_j, pygame.K_w, pygame.K_x, pygame.K_v, pygame.K_r,
            pygame.K_t, pygame.K_p, pygame.K_a, pygame.K_b, pygame.K_c, pygame.K_d, pygame.K_e, pygame.K_f]
    stack = [0] * 16
    display = []
    for i in range(32):
        display.append([0] * 64)
    point_pile = 512
    point_stack = 0
    regI = 0
    delay = 0
    sound = 0
    return display, point_stack, point_pile, register, regI, delay, sound, memory, stack, keys


def romOpen(memory):
    bin = open('PONG', "rb").read()
    n = 0
    while n < len(bin):
        memory[n + 0x200] = bin[n]
        n = n + 1
    return memory
