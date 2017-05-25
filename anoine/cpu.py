from config import
from instructions import
from pygame.local import *


opcode = (memory[pointPile] << 8) + memory[pointPile + 1]


jp.masque[0]= 0x0000; jp.id[0]=0x0FFF;          /* 0NNN / 
  jp.masque[1]= 0xFFFF; jp.id[1]=0x00E0;          / 00E0 / 
  jp.masque[2]= 0xFFFF; jp.id[2]=0x00EE;          / 00EE / 
  jp.masque[3]= 0xF000; jp.id[3]=0x1000;          / 1NNN / 
  jp.masque[4]= 0xF000; jp.id[4]=0x2000;          / 2NNN / 
  jp.masque[5]= 0xF000; jp.id[5]=0x3000;          / 3XNN / 
  jp.masque[6]= 0xF000; jp.id[6]=0x4000;          / 4XNN / 
  jp.masque[7]= 0xF00F; jp.id[7]=0x5000;          / 5XY0 / 
  jp.masque[8]= 0xF000; jp.id[8]=0x6000;          / 6XNN / 
  jp.masque[9]= 0xF000; jp.id[9]=0x7000;          / 7XNN / 
  jp.masque[10]= 0xF00F; jp.id[10]=0x8000;          / 8XY0 / 
  jp.masque[11]= 0xF00F; jp.id[11]=0x8001;          / 8XY1 / 
  jp.masque[12]= 0xF00F; jp.id[12]=0x8002;          / 8XY2 / 
  jp.masque[13]= 0xF00F; jp.id[13]=0x8003;          / BXY3 / 
  jp.masque[14]= 0xF00F; jp.id[14]=0x8004;          / 8XY4 / 
  jp.masque[15]= 0xF00F; jp.id[15]=0x8005;          / 8XY5 / 
  jp.masque[16]= 0xF00F; jp.id[16]=0x8006;          / 8XY6 / 
  jp.masque[17]= 0xF00F; jp.id[17]=0x8007;          / 8XY7 / 
  jp.masque[18]= 0xF00F; jp.id[18]=0x800E;          / 8XYE / 
  jp.masque[19]= 0xF00F; jp.id[19]=0x9000;          / 9XY0 / 
  jp.masque[20]= 0xF000; jp.id[20]=0xA000;          / ANNN / 
  jp.masque[21]= 0xF000; jp.id[21]=0xB000;          / BNNN / 
  jp.masque[22]= 0xF000; jp.id[22]=0xC000;          / CXNN / 
  jp.masque[23]= 0xF000; jp.id[23]=0xD000;          / DXYN */
jp.masque[24]= 0xF0FF; jp.id[24]=0xE09E;          /* EX9E / 
  jp.masque[25]= 0xF0FF; jp.id[25]=0xE0A1;          / EXA1 / 
  jp.masque[26]= 0xF0FF; jp.id[26]=0xF007;          / FX07 / 
  jp.masque[27]= 0xF0FF; jp.id[27]=0xF00A;          / FX0A / 
  jp.masque[28]= 0xF0FF; jp.id[28]=0xF015;          / FX15 / 
  jp.masque[29]= 0xF0FF; jp.id[29]=0xF018;          / FX18 / 
  jp.masque[30]= 0xF0FF; jp.id[30]=0xF01E;          / FX1E / 
  jp.masque[31]= 0xF0FF; jp.id[31]=0xF029;          / FX29 / 
  jp.masque[32]= 0xF0FF; jp.id[32]=0xF033;          / FX33 / 
  jp.masque[33]= 0xF0FF; jp.id[33]=0xF055;          / FX55 / 
  jp.masque[34]= 0xF0FF; jp.id[34]=0xF065;          / FX65 */

masque = [0xF000, 0xFFFF, 0xFFFF, 0xF000, 0xF000, 0xF000, 0xF000, 0xF00F, 0xF000, 0xF000, 0xF00F, 0xF00F, 0xF00F,
            0xF00F, 0xF00F, 0xF00F, 0xF00F, 0xF00F, 0xF00F, 0xF00F, 0xF000, 0xF000, 0xF000, 0xF000, 0xF0FF, 0xF0FF,
            0xF0FF, 0xF0FF, 0xF0FF, 0xF0FF, 0xF0FF, 0xF0FF, 0xF0FF, 0xF0FF, 0xF0FF]

idOpcode = [0x0FFF, 0x00E0, 0x00EE, 0x1000, 0x2000, 0x3000, 0x4000, 0x5000, 0x6000, 0x7000, 0x8000, 0x8001, 0x8002,
            0x8003, 0x8004, 0x8005, 0x8006, 0x8007, 0x800E, 0x9000, 0xA000, 0xB000, 0xC000, 0xD000, 0xE09E, 0xE0A1,
            0xF007, 0xF00A, 0xF015, 0xF018, 0xF01E, 0xF029, 0xF033, 0xF055, 0xF065]


#1	charger rom memory
#2	début => pointPile = 512
#3	charger 8 bit par 8 bit
#512 sont les 8 premiers bits     513 Seconds bits
#apres avoir en memoire instructions et pas dépasser 255
#cree fonctin genere opcode (discord cassou) return opcode
#2 eme fcton param opcode
#2 var id opcode et mask
#parcour liste mask
#for i in range mask
#pos PinteurPile stk pos pile 1