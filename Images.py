from PIL import Image
import pygame
from Assets import block_s

''' Init the images relevent'''
all = Image.open('assets/snakeset.png')
P_Tree = all.crop((0,0,64,64))
P_Tree = P_Tree.resize((block_s,block_s))
P_Tree = pygame.image.fromstring(P_Tree.tobytes(), P_Tree.size, P_Tree.mode).convert_alpha()
P_Grass = all.crop((0,64,64,128))
P_Grass = P_Grass.resize((block_s,block_s))
P_Grass = pygame.image.fromstring(P_Grass.tobytes(), P_Grass.size, P_Grass.mode).convert_alpha()
P_Corner_DR = all.crop((65,0,129,64))
P_Corner_DR = P_Corner_DR.resize((block_s,block_s))
P_Corner_DR = pygame.image.fromstring(P_Corner_DR.tobytes(), P_Corner_DR.size, P_Corner_DR.mode).convert_alpha()
P_Corner_DL = all.crop((192,0,256,64))
P_Corner_DL = P_Corner_DL.resize((block_s,block_s))
P_Corner_DL = pygame.image.fromstring(P_Corner_DL.tobytes(), P_Corner_DL.size, P_Corner_DL.mode).convert_alpha()
P_Corner_UR = all.crop((128,64,192,128))
P_Corner_UR = P_Corner_UR.resize((block_s,block_s))
P_Corner_UR = pygame.image.fromstring(P_Corner_UR.tobytes(), P_Corner_UR.size, P_Corner_UR.mode).convert_alpha()
P_Corner_UL = all.crop((192,64,256,128))
P_Corner_UL = P_Corner_UL.resize((block_s,block_s))
P_Corner_UL = pygame.image.fromstring(P_Corner_UL.tobytes(), P_Corner_UL.size, P_Corner_UL.mode).convert_alpha()
P_Apple = all.crop((192,128,256,192))
P_Apple = P_Apple.resize((block_s,block_s))
P_Apple = pygame.image.fromstring(P_Apple.tobytes(), P_Apple.size, P_Apple.mode).convert_alpha()
#P_Snake_H = all.crop((128,0,192,64))
#P_Snake_H = P_Snake_H.resize((block_s,block_s))
#P_Snake_H = pygame.image.fromstring(P_Snake_H.tobytes(), P_Snake_H.size, P_Snake_H.mode).convert_alpha()
P_Snake_V = all.crop((64,64,128,128))
P_Snake_V = P_Snake_V.resize((block_s,block_s))
P_Snake_V = pygame.image.fromstring(P_Snake_V.tobytes(), P_Snake_V.size, P_Snake_V.mode).convert_alpha()
P_Snake_H = pygame.transform.rotate(P_Snake_V, 90)
P_Tail = all.crop((0,128,64,192))
P_Tail = P_Tail.resize((block_s,block_s))
P_Tail_LEFT = pygame.image.fromstring(P_Tail.tobytes(), P_Tail.size, P_Tail.mode).convert_alpha()
P_Tail_UP = pygame.transform.rotate(P_Tail_LEFT, 270)
P_Tail_DOWN = pygame.transform.rotate(P_Tail_LEFT, 90)
P_Tail_RIGHT = pygame.transform.rotate(P_Tail_LEFT, 180)
P_Head = all.crop((64,128,128,192))
P_Head = P_Head.resize((block_s,block_s))
P_Head_DOWN = pygame.image.fromstring(P_Head.tobytes(), P_Head.size, P_Head.mode).convert_alpha()
P_Head_UP = pygame.transform.rotate(P_Head_DOWN, 180)
P_Head_RIGHT = pygame.transform.rotate(P_Head_DOWN, 90)
P_Head_LEFT = pygame.transform.rotate(P_Head_DOWN, 270)

# 10 - 'Horizontal snake',11 - 'Vertical snake',12 - 'UP RIGHT',13 - 'UP LEFT',14 - 'DOWN RIGHT',15 - 'DOWN LEFT'
        # 20 - 'Head Up', 21 - 'Head Down', 22 - 'Head Left', 23 - 'Head Right'
        # 30 - 'Tail Up', 31 - 'Tail Down', 32 - 'Tail Left', 33 - 'Tail Right'
        # 1 - 'Apple'
convert_images = {'10':'0', '11':'1', '12':'2', '13':'3', '14':'4', '15':'5', '20':'6', '21':'7', '22':'8',
                        '23': '9', '30': '10', '31': '11', '32': '12', '33': '13', '1': '14'}
Snake_images = [P_Snake_H, P_Snake_V, P_Corner_UR, P_Corner_UL, P_Corner_DR, P_Corner_DL, P_Head_UP, P_Head_DOWN,
                P_Head_LEFT, P_Head_RIGHT, P_Tail_UP, P_Tail_DOWN, P_Tail_LEFT, P_Tail_RIGHT, P_Apple]

background_images = [P_Tree, P_Grass]
''' END'''

