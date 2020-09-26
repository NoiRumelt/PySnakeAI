

'''Init Parameters, Changeable'''
board_size = 15,10  #2D array to create, Col X Row
block_s = 16        #The size of the grid box
background_ratios = (0.3, 0.7) #The chance of getting Tree, Grass
hovers, hoverA, hovere, hoverm = (200,200,200), (200,200,200), (200,200,200), (200,200,200)
TICKING_menus = 30
TICKING_game = 30
SPEED = 200
gen_width, gen_height = 4, 4
'''END'''
'''Calc some parameters, don't touch'''
gen_size = gen_width * gen_height
b_width, b_height = board_size
if 15 > b_width or 10 > b_height:
    b_width, b_height = board_size = 15, 10
Started = False
dimensions = pixel_width, pixel_height = (b_width * block_s * gen_width) + (gen_width - 1) * 5, (b_height * block_s * gen_height) + (gen_height - 1) * 5 + 100
ticking = TICKING_menus




