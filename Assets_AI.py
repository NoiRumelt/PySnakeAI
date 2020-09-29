from typing import Union
import numpy as np
'''Init Parameters, Changeable'''
board_size = 15,10  #2D array to create, Col X Row
block_s = 16        #The size of the grid box
background_ratios = (0.3, 0.7) #The chance of getting Tree, Grass
hovers, hoverA, hovere, hoverm = (200,200,200), (200,200,200), (200,200,200), (200,200,200)
TICKING_menus = 30
TICKING_game = 30
SPEED = 1000
gen_width, gen_height = 4, 4
'''END'''
'''Calc some parameters, don't touch'''

up = np.zeros((4,1))
up[0,0] = 1.0
down = np.zeros((4, 1))
down[1, 0] = 1.0
right = np.zeros((4, 1))
right[3, 0] = 1.0
left = np.zeros((4, 1))
left[2, 0] = 1.0

Dir_vector_lib = {'u': up, 'd': down, 'l': left, 'r': right}
b_width, b_height = board_size
if 15 > b_width or 10 > b_height:
    b_width, b_height = board_size = 15, 10
Started = False
dimensions = pixel_width, pixel_height = (b_width * block_s * gen_width) + (gen_width - 1) * 5, (b_height * block_s * gen_height) + (gen_height - 1) * 5 + 100
ticking = TICKING_menus

class Slope(object):
    __slots__ = ('rise', 'run')
    def __init__(self, rise: int, run: int):
        self.rise = rise
        self.run = run

class Vision(object):
    __slots__ = ('dist_to_wall', 'dist_to_apple', 'dist_to_self')

    def __init__(self,
                 dist_to_wall: Union[float, int],
                 dist_to_apple: Union[float, int],
                 dist_to_self: Union[float, int]
                 ):
        self.dist_to_wall = float(dist_to_wall)
        self.dist_to_apple = float(dist_to_apple)
        self.dist_to_self = float(dist_to_self)


VISION_8 = (
    Slope(-1, 0), Slope(-1, 1),
    Slope(0, 1), Slope(1, 1),
    Slope(1, 0),  Slope(1, -1),
    Slope(0, -1), Slope(-1, -1)
)



