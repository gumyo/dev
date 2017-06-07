import instruction as iN
from config import iniVar, timers
import pygame
import sys
from gui import *
from random import randint
from pygame import *


def opCode(point_pile, memory):
	return (memory[point_pile] << 8) + memory[point_pile + 1]  #check


def id(opcode):
	mask_block_un = 0xF000
	mask_block_deux = 0xF00F
	mask_block_trois = 0xF0FF
	masks = (mask_block_un, mask_block_deux, mask_block_trois)
	block_instructions_un = [0x1000, 0x2000, 0x3000, 0x4000, 0x5000, 0x6000, 0x7000, 0x9000, 0xA000, 0xB000, 0xC000,
							 0xD000]
	block_instructions_deux = [0x8000, 0x8001, 0x8002, 0x8003, 0x8004, 0x8005, 0x8006, 0x8007, 0x800E]
	block_instructions_trois = [0x00E0, 0x00EE, 0xE09E, 0xE0A1, 0xF007, 0xF00A, 0xF015, 0xF018, 0xF01E, 0xF029, 0xF033,
								0xF055, 0xF065]
	instructions = (block_instructions_un, block_instructions_deux, block_instructions_trois)
	for i in range(3):
		for nombre in range(len(instructions[i])):
			if opcode & masks[i] == instructions[i][nombre]:
				return instructions[i][nombre] #check


def mainCPU():
	global display, point_stack, point_pile, register, regI, delay, sound, memory, stack, screen, keys
	opcode = opCode(point_pile, memory)
	instruction = id(opcode)
	if instruction == 0x00E0:
		display = iN.clear()
	elif instruction == 0x00EE:
		point_stack, point_pile, stack = iN.ret(point_stack, point_pile, stack)
	elif instruction == 0x1000:
		point_pile = iN.jump(opcode)
	elif instruction == 0x2000:
		point_pile, point_stack, stack = iN.call(opcode, point_pile, point_stack, stack)
	elif instruction == 0x3000:
		point_pile = iN.next(opcode, register, point_pile)
	elif instruction == 0x4000:
		point_pile = iN.nextNot(opcode, register, point_pile)
	elif instruction == 0X5000:
		point_pile = iN.nextReg(opcode, register, point_pile)
	elif instruction == 0x6000:
		register = iN.setNnVx(opcode, register)
	elif instruction == 0x7000:
		register = iN.addNnVx(opcode, register)
	elif instruction == 0x8000:
		register = iN.setVxVy(opcode, register)
	elif instruction == 0x8001:
		register = setVxOrVy(opcode, register)
	elif instruction == 0x8002:
		register = iN.setVxAndVy(opcode, register)
	elif instruction == 0x8003:
		register = iN.setVxXorVy(opcode, register)
	elif instruction == 0x8004:
		register = iN.addVyVx(opcode, register)
	elif instruction == 0x8005:
		register = iN.subVyVx(opcode, register)
	elif instruction == 0x8006:
		register = iN.decVxRight(opcode, register)
	elif instruction == 0x8007:
		register = iN.subVxVy(opcode, register)
	elif instruction == 0x800E:
		register = iN.decVxLeft(opcode, register)
	elif instruction == 0x9000:
		point_pile = iN.jmpIfVxNoVy(opcode, register, point_pile)
	elif instruction == 0xA000:
		regI = iN.nnnI(opcode)
	elif instruction == 0xB000:
		point_pile = iN.nnnVo(opcode, register)
	elif instruction == 0xC000:
		register = iN.rndVx(opcode, register)
	elif instruction == 0xD000:
		display, register = iN.drawDisplay(opcode, register, screen, display, memory, regI)
	elif instruction == 0xE09E:
		point_pile = iN.keyVxYes(opcode, register, keys, point_pile)
	elif instruction == 0xE0A1:
		point_pile = iN.keyVxNo(opcode, register, keys, point_pile)
	elif instruction == 0xF007:
		register = iN.tmpVx(opcode, register, delay)
	elif instruction == 0xF00A:
		register = iN.key(opcode, register, keys)
	elif instruction == 0xF015:
		delay = iN.vxTmp(opcode, register)
	elif instruction == 0xF018:
		sound = iN.soundVx(opcode, register)
	elif instruction == 0xF01E:
		regI, register = iN.addIVx(opcode, register, regI)
	elif instruction == 0xF029:
		regI = iN.IdgtVx(opcode, register)
	elif instruction == 0xF033:
		memory = iN.stkVxI(opcode, register, regI, memory)
	elif instruction == 0xF055:
		memory = iN.stkVoVx(opcode, register, regI, memory)
	elif instruction == 0xF065:
		memory = iN.repVoVx(opcode, register, regI, memory)
	print(hex(instruction))
	point_pile += 2


def module(action1, action2, action3):
	if action1:
		action1 = run()
	if action2:
		gui_register(register, screen)
	if action3:
		action3 = gui_memory(memory)
	return action1, action2, action3

def main():
	global display, point_stack, point_pile, register, regI, delay, sound, memory, stack, screen, keys
	pygame.init()
	action1, action2, action3 = False, False, False
	screen = pygame.display.set_mode((1920, 320))
	display, point_stack, point_pile, register, regI, delay, sound, memory, stack, keys = iniVar()
	timer = pygame.USEREVENT + 1
	pygame.time.set_timer(timer, 17)
	while True:
		mainCPU()
		for event in pygame.event.get():
			if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
				pygame.quit()
				sys.exit()
			if event.type == timer:
				delay, sound = timers(delay, sound)
			if event.type == KEYDOWN and event.key == K_F1:
				action1 = True
			if event.type == KEYDOWN and event.key == K_F2:
				if action2 == False:
					action2 = True
				else:
					action2 = False
					screen.fill((0,0,0,255), (650, 20, 1920, 20))
			if event.type == KEYDOWN and event.key == K_F3:
					action3 = True

		action1, action2, action3 = module(action1, action2, action3)

main()
