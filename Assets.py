

'''Init Parameters, Changeable'''
board_size = 15,10  #2D array to create, Col X Row
block_s = 32        #The size of the grid box
background_ratios = (0.3, 0.7) #The chance of getting Tree, Grass
hovers, hoverA, hovere, hoverm = (200,200,200), (200,200,200), (200,200,200), (200,200,200)
TICKING_menus = 30
TICKING_game = 30
SPEED = 200
'''END'''
'''Calc some parameters, don't touch'''
b_width, b_height = board_size
if 15 > b_width or 10 > b_height:
    b_width, b_height = board_size = 15, 10
Started = False
dimensions = pixel_width, pixel_height = b_width * block_s, b_height * block_s
ticking = TICKING_menus




