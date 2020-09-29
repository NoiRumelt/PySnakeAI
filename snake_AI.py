from PIL import Image
import numpy as np
import sys
from typing import Optional, Union, List
import pygame as pg
from Assets_AI import *
from random import choices, randrange
from NeuralNetwork import *

'''PyGame Init'''
pg.init()
screen = pg.display.set_mode((dimensions))
clock = pg.time.Clock()
game_font = pg.font.Font('04B_19.ttf',40)
STEPEVENT = pg.USEREVENT
pg.time.set_timer(STEPEVENT, SPEED)

from Images_AI import *



class Snake:

    def __init__(self, row, col):
        self.Pos = [np.array([row // 2, col // 2]), np.array([row // 2 + 1, col // 2])]
        self.Direction = np.array([-1,0])   # The options are: 'u' - Up, 'd' - Down, 'l' - Left, 'r' - Right
        self.Direction_char = 'u'
        self.Direction_wait = 'u'
        self.Head_dir_vector = Dir_vector_lib['u']
        self.Tail_dir_vector = Dir_vector_lib['u']
        self.length = 2
        self.steps_made = 0
        self._fitness = 0
        self.Dir_tra = {'u': np.array([-1, 0]), 'l': np.array([0, -1]), 'd': np.array([1, 0]), 'r': np.array([0, 1])}
        self.possible_directions = ('u', 'l', 'd', 'r')

    def __repr__(self):
        return self.Pos, self.Direction

    def __len__(self):
        return self.length

    def calculate_fitness(self):
        # Give positive minimum fitness for roulette wheel selection
        score = self.length - 2
        self._fitness = (self.steps_made) + ((2 ** score) + (score ** 2.1) * 500) - (
                    ((.25 * self.steps_made) ** 1.3) * (score ** 1.2))
        self._fitness = max(self._fitness, .1)
        return self._fitness

    def get_fitness(self):
        return self._fitness

    def step(self, Apple_pos):
        # No Input, taking the current position of the snake and the current direction of it, and change the 2D array,
        # moving the snake 1 step ahead, drawing the new head, deleting the the tail. not checking for collisions.
        # updating the snake length.
        Ate = False
        last = self.Pos[-1]
        for part in range(0, self.length):
            if part == 0:
                save = self.Pos[part].copy()
                if self.Col_W_Wall(): return False, False
                if self.Col_W_Self(): return False, False
                self.Pos[part] += self.Direction
                self.Direction_char = self.Direction_wait
                if (self.Pos[part] == Apple_pos).all(): Ate = True # Ate the Apple?
            else:
                save = self.Pos[part].copy()
                self.Pos[part] = temp
            temp = save
        if Ate:
            self.Pos.append(last)
            self.length += 1
            return True, True
        self.steps_made += 1
        return True, False
    def Col_W_Wall(self):
        return b_height <= self.Pos[0][0] + self.Direction[0] or \
        self.Pos[0][0] + self.Direction[0] < 0 or \
        b_width <= self.Pos[0][1] + self.Direction[1] or \
        self.Pos[0][1] + self.Direction[1] < 0
    def Col_W_Self(self):
        intendedPos = self.Pos[0] + self.Direction
        for part in range (0, self.length - 1):
            if (self.Pos[part] == intendedPos).all(): return True
        return False
    def get_dir(self):
        return self.Direction_char
    def get_pos_part(self, part):
        # Input - part of the snake
        # Output - tuple of the row and the col of this part
        return self.Pos[part][0], self.Pos[part][1]
    def get_part_identity(self, part):
        # 10 - 'Horizontal snake',11 - 'Vertical snake',12 - 'UP RIGHT',13 - 'UP LEFT',14 - 'DOWN RIGHT',15 - 'DOWN LEFT'
        # 20 - 'Head Up', 21 - 'Head Down', 22 - 'Head Left', 23 - 'Head Right'
        # 30 - 'Tail Up', 31 - 'Tail Down', 32 - 'Tail Left', 33 - 'Tail Right'
        if part == 0:
            if self.Direction_char == 'u':
                self.Head_dir_vector = Dir_vector_lib['u']  # up
                return 20
            if self.Direction_char == 'd':
                self.Head_dir_vector = Dir_vector_lib['d']  # down
                return 21
            if self.Direction_char == 'l':
                self.Head_dir_vector = Dir_vector_lib['l']  # left
                return 22
            if self.Direction_char == 'r':
                self.Head_dir_vector = Dir_vector_lib['d']  # down
                return 23
        elif part == self.length - 1:
            if (self.Pos[part] == (self.Pos[part - 1] + self.Dir_tra['u'])).all():
                self.Tail_dir_vector = Dir_vector_lib['d']  # down
                return 31
            if (self.Pos[part] == (self.Pos[part - 1] + self.Dir_tra['d'])).all():
                self.Tail_dir_vector = Dir_vector_lib['u']  # up
                return 30
            if (self.Pos[part] == (self.Pos[part - 1] + self.Dir_tra['l'])).all():
                self.Tail_dir_vector = Dir_vector_lib['r']  # right
                return 33
            if (self.Pos[part] == (self.Pos[part - 1] + self.Dir_tra['r'])).all():
                self.Tail_dir_vector = Dir_vector_lib['l']  # left
                return 32
        else:
            if (self.Pos[part] == self.Pos[part - 1] + self.Dir_tra['d']).all() or \
                    (self.Pos[part] == self.Pos[part + 1] + self.Dir_tra['d']).all():
                if (self.Pos[part] == self.Pos[part - 1] + self.Dir_tra['u']).all() or \
                        (self.Pos[part] == self.Pos[part + 1] + self.Dir_tra['u']).all(): return 11
                if (self.Pos[part] == self.Pos[part - 1] + self.Dir_tra['r']).all() or \
                        (self.Pos[part] == self.Pos[part + 1] + self.Dir_tra['r']).all(): return 13
                if (self.Pos[part] == self.Pos[part - 1] + self.Dir_tra['l']).all() or \
                        (self.Pos[part] == self.Pos[part + 1] + self.Dir_tra['l']).all(): return 12
            if (self.Pos[part] == self.Pos[part - 1] + self.Dir_tra['u']).all() or \
                    (self.Pos[part] == self.Pos[part + 1] + self.Dir_tra['u']).all():
                if (self.Pos[part] == self.Pos[part - 1] + self.Dir_tra['r']).all() or \
                        (self.Pos[part] == self.Pos[part + 1] + self.Dir_tra['r']).all(): return 15
                if (self.Pos[part] == self.Pos[part - 1] + self.Dir_tra['l']).all() or \
                        (self.Pos[part] == self.Pos[part + 1] + self.Dir_tra['l']).all(): return 14
            if (self.Pos[part] == self.Pos[part - 1] + self.Dir_tra['r']).all() or \
                    (self.Pos[part] == self.Pos[part + 1] + self.Dir_tra['r']).all():
                if (self.Pos[part] == self.Pos[part - 1] + self.Dir_tra['l']).all() or \
                    (self.Pos[part] == self.Pos[part + 1] + self.Dir_tra['l']).all(): return 10

    def C_dir(self, dir):
        # Changing the direction of the moving of the snake, Checking if we haven't choose the body of the snake direction
            if dir == 'u' and not (self.Pos[0] + self.Dir_tra['u'] == self.Pos[1]).all():
                self.Direction = self.Dir_tra['u']
                self.Direction_wait = 'u'
            if dir == 'd' and not (self.Pos[0] + self.Dir_tra['d'] == self.Pos[1]).all():
                self.Direction = self.Dir_tra['d']
                self.Direction_wait = 'd'
            if dir == 'l' and not (self.Pos[0] + self.Dir_tra['l'] == self.Pos[1]).all():
                self.Direction = self.Dir_tra['l']
                self.Direction_wait = 'l'
            if dir == 'r' and not (self.Pos[0] + self.Dir_tra['r'] == self.Pos[1]).all():
                self.Direction = self.Dir_tra['r']
                self.Direction_wait = 'r'

class Apple():
    # Defining the Apple, Position
    def __init__(self, columns, rows, snake_pos):
        # Creating the apple, choosing a position for the apple on the board not outside the borders and not on the snake.
        while True:
            exist = False
            rndPos = np.array([randrange(0, rows - 1), randrange(0, columns - 1)])
            for part in snake_pos:
                if (rndPos == part).all():
                    exist = True
            if exist:
                continue
            break
        self.Pos = rndPos

    def get_pos(self):
        return self.Pos[0], self.Pos[1]



class Board:
    def __init__(self, dim):
        # Creating a 2D array represent the snake and the apple
        self.rows, self.columns = dim
        self.board_array = np.full((self.rows, self.columns), 0)
        self.E_snake = Snake(self.rows, self.columns)
        self.apple = Apple(self.columns, self.rows, self.E_snake.Pos)
        self.NN_array = np.full((self.rows, self.columns), 0)
        self.vision: List[Vision] = [None] * 8
        self.vision_nn_array: np.ndarray = np.zeros((32, 1))

    def get_board_array(self):
        # returning a 2D numpy array which illustrate the current condition of the board: snake, apples, etc...
        # 10 - 'Horizontal snake',11 - 'Vertical snake',12 - 'UP RIGHT',13 - 'UP LEFT',14 - 'DOWN RIGHT',15 - 'DOWN LEFT'
        # 20 - 'Head Up', 21 - 'Head Down', 22 - 'Head Left', 23 - 'Head Right'
        # 30 - 'Tail Up', 31 - 'Tail Down', 32 - 'Tail Left', 33 - 'Tail Right'
        return self.board_array

    def update_board(self):
        # using the snake and the apple positions to update the board to the code of images
        '''Handle the snake'''
        self.board_array = np.full((self.rows, self.columns), 0)
        for part in range(0, len(self.E_snake)):
            self.board_array[self.E_snake.get_pos_part(part)] = self.E_snake.get_part_identity(part)
            self.NN_array[self.E_snake.get_pos_part(part)] = 1

        if self.apple is not None: # Writes 1 on the board on the position of the apple
            self.board_array[self.apple.get_pos()] = 1
            self.NN_array[self.apple.get_pos()] = 2

    def get_vision_vector(self):
        return self.vision_nn_array

    def calc_vision_vector(self):
        # Split _vision into np array where rows [0-2] are _vision[0].dist_to_wall, _vision[0].dist_to_apple, _vision[0].dist_to_self,
        # rows [3-5] are _vision[1].dist_to_wall, _vision[1].dist_to_apple, _vision[1].dist_to_self, etc. etc. etc.
        for va_index, v_index in zip(range(0, 8 * 3, 3), range(8)):
            vision = self.vision[v_index]
            self.vision_nn_array[va_index, 0] = vision.dist_to_wall
            self.vision_nn_array[va_index + 1, 0] = vision.dist_to_apple
            self.vision_nn_array[va_index + 2, 0] = vision.dist_to_self

        i = 24  # Start at the end

        head_direction = self.E_snake.Head_dir_vector
        # One-hot encode direction
        self.vision_nn_array[i: i + 4] = head_direction

        i += 4

        # One-hot tail direction
        head_direction = self.E_snake.Tail_dir_vector
        self.vision_nn_array[i: i + 4] = head_direction

    def look(self):
        # Look all around
        for i, slope in enumerate(VISION_8):

            dir_i_vision = self.look_in_direction(slope)
            self.vision[i] = dir_i_vision
            #print(i, slope.rise, slope.run)
            #print(dir_i_vision.dist_to_wall,dir_i_vision.dist_to_apple,dir_i_vision.dist_to_self)

        # Update the input array
        self.calc_vision_vector()

    def _within_wall(self, position) -> bool:
        return 0 <= position[0] < self.rows and 0 <= position[1] < self.columns

    def _is_body_location(self, position) -> bool:
        for i in range(len(self.E_snake)):
            if (position == self.E_snake.get_pos_part(i)).all():
                return True
        return False


    def _is_apple_location(self, position) -> bool:
        return (position == self.apple.Pos).all()

    def look_in_direction(self, slope: Slope):
        dist_to_wall = None
        dist_to_apple = np.inf
        dist_to_self = np.inf

        wall_location = None
        apple_location = None
        self_location = None

        position = np.copy(self.E_snake.get_pos_part(0))
        #print (position)
        distance = 1.0
        total_distance = 0.0

        # Can't start by looking at yourself
        position[1] += slope.run
        position[0] += slope.rise
        total_distance += distance
        body_found = False  # Only need to find the first occurance since it's the closest
        food_found = False  # Although there is only one food, stop looking once you find it

        # Keep going until the position is out of bounds
        while self._within_wall(position):

            if not body_found and self._is_body_location(position):
                dist_to_self = total_distance
                self_location = np.copy(position)
                body_found = True
            if not food_found and self._is_apple_location(position):
                dist_to_apple = total_distance
                apple_location = np.copy(position)
                food_found = True

            wall_location = position
            position[1] += slope.run
            position[0] += slope.rise
            total_distance += distance
        assert (total_distance != 0.0)

        dist_to_wall = 1.0 / total_distance
        dist_to_apple = 1.0 if dist_to_apple != np.inf else 0.0
        dist_to_self = 1.0 if dist_to_self != np.inf else 0.0

        vision = Vision(dist_to_wall, dist_to_apple, dist_to_self)
        return vision

    def step(self, apple):
        return self.E_snake.step(apple)

    def C_dir(self, dir):
        self.E_snake.C_dir(dir)


    def Grow_Apple(self):
        self.apple = Apple(self.columns, self.rows, self.E_snake.Pos)
    def Ate_T_Apple(self):
        self.apple = None
    def get_apple_exist(self):
        return self.apple != None
    def get_apple_pos(self):
        return self.apple.get_pos()

def Draw_Board(board_local):
    # Returns Pygame surface representing the specific board
    board_surface = pg.Surface(((b_width * block_s), (b_height * block_s)), pg.SRCALPHA).convert_alpha()
    for c in range(0, b_width):
        for r in range(0, b_height):
            x_o = c * block_s
            y_o = r * block_s
            if board_local[r,c] != 0:
                image = Snake_images[int(convert_images[str(board_local[r,c])])]
                board_surface.blit(image, (x_o, y_o))
    return board_surface

def Draw_Gen_Board(gen_board):
    # input: Generation Board
    # output: surface to print on the screen
    gen_board_surface = pg.Surface(((b_width * block_s * gen_width) + (gen_width - 1) * 5,
                                 (b_height * block_s * gen_height) + (gen_height - 1) * 5), pg.SRCALPHA).convert_alpha()
    x_o, y_o = 0, 0
    for r in range(0, gen_height):
        x_o = 0
        for c in range(0, gen_width):
            gen_board_surface.blit(Draw_Board(gen_board.boards[r, c].get_board_array()), (x_o,y_o))
            x_o = x_o + b_width * block_s
            x_o += 5
        y_o = y_o + b_height * block_s
        if r < gen_height - 1:
            y_o += 5
    return gen_board_surface


def Create_BG(images,ratios):
    # Gets dimensions with tuple, list of background pictures and ratios.
    #  returning a surface using those Pictures
    bg_surface = pg.Surface(((b_width * block_s), (b_height * block_s))).convert_alpha()
    for x in range(0, b_width):
        for y in range(0, b_height):
            x_o = x * block_s
            y_o = y * block_s
            choice = choices(images,ratios,k = 1)
            bg_surface.blit(choice[0], (x_o,y_o))
    return bg_surface

def Create_Gen_Background(backgroundSurface):
    # output: surface of the background surface of all of the board
    gen_bg_surface = pg.Surface(((b_width * block_s * gen_width) + (gen_width - 1) * 5, (b_height * block_s * gen_height) + (gen_height - 1) * 5)).convert_alpha()
    x_o, y_o = 0, 0
    for x in range(0, gen_width):
        y_o = 0
        for y in range(0, gen_height):
            gen_bg_surface.blit(backgroundSurface, (x_o,y_o))
            y_o = y_o + b_height * block_s
            y_o += 5
        x_o = x_o + b_width * block_s
        if x < gen_width - 1:
            x_o += 5
    return gen_bg_surface

def QUIT_snake():
    pg.quit()
    sys.exit()

class Generation_Board():
    def __init__(self, gen_cols, gen_rows, b_cols, b_rows):
        self.boards = np.empty((gen_rows, gen_cols), dtype=object)
        self.models = np.empty((gen_rows, gen_cols), dtype=object)
        self.possible_directions = ('u', 'd', 'l', 'r')
        for c in range(0, gen_cols):
            for r in range(0, gen_rows):
                self.boards[r, c] = Board((b_rows, b_cols))
                self.models[r, c] = create_model()
        self.live = np.full((gen_rows, gen_cols), True)
        self.gen_still_alive = True
        self.fitness = np.full((gen_rows, gen_cols), 0)

    def step(self):
        count = 0
        for r in range(0, gen_width):
            for c in range(0, gen_height):
                if self.live[r, c]:
                    E_board = self.boards[r, c]
                    if not E_board.get_apple_exist():
                        E_board.Grow_Apple()
                    E_board.look()
                    nn_rec_dir = predict_action(E_board.vision_nn_array, self.models[r, c])
                    nn_rec_dir = self.possible_directions[np.argmax(nn_rec_dir)]
                    E_board.C_dir(nn_rec_dir)
                    count += 1
                    game_active, ate = E_board.step(E_board.get_apple_pos())
                    if not game_active:
                        self.live[r, c] = False
                    if ate:
                        E_board.Ate_T_Apple()
        if count == 0:
            self.gen_still_alive = False


    def update_board(self):
        for r in range(0, gen_width):
            for c in range(0, gen_height):
                self.boards[r, c].update_board()

    def calc_gen_fitness(self):
        for r in range(0, gen_width):
            for c in range(0, gen_height):
                e_board = self.boards[r, c]
                self.fitness[r, c] = e_board.E_snake.calculate_fitness()


def create_new_gen(generation: Generation_Board) -> Generation_Board:

    fitness_array = generation.fitness
    chosen_parents = [None, None, None, None]

    for i in range(4):
        result = np.where(fitness_array == np.amax(fitness_array))
        position_of_max_fitness = (result[0][0], result[1][0])
        chosen_parents[i] = generation.models[position_of_max_fitness]
        fitness_array[result[0][0], result[1][0]] = 0



'''PyGame LOOP'''

BackGround_AI_surface = Create_Gen_Background(Create_BG(background_images, background_ratios))
generation_board = Generation_Board(gen_width, gen_height, b_width, b_height)
generation_board.update_board()
genNum = 1 # options - menu, game, gameover
MakeStep = False
ticking = TICKING_game
while True:

    screen.blit(BackGround_AI_surface, (0, 0))
    Generation_AI_surface = Draw_Gen_Board(generation_board)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
            pg.quit()
        if event.type == STEPEVENT:
            if generation_board.gen_still_alive:
                generation_board.step()
            else:
                generation_board.calc_gen_fitness()
                #print(generation_board.fitness)
                #generation_board = create_new_gen(generation_board)




        generation_board.update_board()

    screen.blit(Generation_AI_surface, (0, 0))
    pg.display.update()
    clock.tick(30)
