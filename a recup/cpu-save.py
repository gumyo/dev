import instruction as iN 

def nonalacon(pointPile, memory):
	return (mem[pointeurPile] << 8) + mem[pointeurPile + 1]

def id():
	mask_block_un = 0xF000
	mask_block_deux = 0xF00F
	mask_block_trois = 0xF0FF
	masks = (mask_block_un, mask_block_deux, mask_block_trois)

	block_instructions_un = {
		0x1000: iN.jump_to_address,  # 1nnn - JUMP nnn
		0x2000: iN.jump_to_subroutine,  # 2nnn - CALL nnn
		0x3000: iN.skip_if_reg_equal_val,  # 3snn - SKE  Vs, nn
		0x4000: iN.skip_if_reg_not_equal_val,  # 4snn - SKNE Vs, nn
		0x5000: iN.skip_if_reg_equal_reg,  # 5st0 - SKE  Vs, Vt
		0x6000: iN.move_value_to_reg,  # 6snn - LOAD Vs, nn
		0x7000: iN.add_value_to_reg,  # 7snn - ADD  Vs, nn
		0x9000: iN.skip_if_reg_not_equal_reg,  # 9st0 - SKNE Vs, Vt
		0xA000: iN.load_index_reg_with_value,  # Annn - LOAD I, nnn
		0xB000: iN.jump_to_index_plus_value,  # Bnnn - JUMP [I] + nnn
		0xC000: iN.generate_random_number,  # Ctnn - RAND Vt, nn
		0xD000: iN.draw_sprite,  # Dstn - DRAW V		
	}

	block_instructions_deux = {
		0x8000: iN.move_reg_into_reg,  # 8st0 - LOAD Vs, Vt
		0x8001: iN.logical_or,  # 8st1 - OR   Vs, Vt
		0x8002: iN.logical_and,  # 8st2 - AND  Vs, Vt
		0x8003: iN.exclusive_or,  # 8st3 - XOR  Vs, Vt
		0x8004: iN.add_reg_to_reg,  # 8st4 - ADD  Vs, Vt
		0x8005: iN.subtract_reg_from_reg,  # 8st5 - SUB  Vs, Vt
		0x8006: iN.right_shift_reg,  # 8st6 - SHR  Vs
		0x8007: iN.subtract_reg_from_reg1,  # 8st7 - SUBN Vs, Vt
		0x800E: iN.left_shift_reg,  # 8stE - SHL  Vs
	}

	block_instructions_trois = {
		0x00E0: iN.clear_return,  # 0nnn - SYS  nnn
		0x00EE: iN.clear_return,  # 0nnn - SYS  nnn
		0xE09E: iN.keyboard_routines,  # see subfunctions below
		0xE0A1: iN.keyboard_routines,  # see subfunctions below
		0xF007: iN.move_delay_timer_into_reg,  # Ft07 - LOAD Vt, DELAY
		0xF00A: iN.wait_for_keypress,  # Ft0A - KEYD Vt
		0xF015: iN.move_reg_into_delay_timer,  # Fs15 - LOAD DELAY, Vs
		0xF018: iN.move_reg_into_sound_timer,  # Fs18 - LOAD SOUND, Vs
		0xF01E: iN.add_reg_into_index,  # Fs1E - ADD  I, Vs
		0xF029: iN.load_index_with_reg_sprite,  # Fs29 - LOAD I, Vs
		0xF033: iN.store_bcd_in_memory,  # Fs33 - BCD
		0xF055: iN.store_regs_in_memory,  # Fs55 - STOR [I], Vs
		0xF065: iN.read_regs_from_memory,  # Fs65 - LOAD Vs, [I]
	}
	instructions = (block_instructions_un, block_instructions_deux, block_instructions_trois)
	return masks, instructions