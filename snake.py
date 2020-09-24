from PIL import Image
import numpy as np
import sys
import pygame as pg
from Assets import *
from random import choices, randrange
'''PyGame Init'''
pg.init()
screen = pg.display.set_mode((dimensions))
clock = pg.time.Clock()
game_font = pg.font.Font('04B_19.ttf',40)
STEPEVENT = pg.USEREVENT
pg.time.set_timer(STEPEVENT, SPEED)

from Images import *

class Snake():
    def __init__(self, row,col):
        self.Pos = [np.array([row // 2, col // 2]), np.array([row // 2 + 1, col // 2])]
        self.Direction = np.array([-1,0]) # The options are: 'u' - Up, 'd' - Down, 'l' - Left, 'r' - Right
        self.Direction_char = 'u'
        self.Direction_wait = 'u'
        self.length = 2
        self.Dir_tra = {'u':np.array([-1,0]), 'l':np.array([0,-1]), 'd':np.array([1,0]), 'r':np.array([0,1])}

    def __repr__(self):
        return self.Pos, self.Direction

    def __len__(self):
        return self.length
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
                if (self.Pos[part] == Apple_pos).all(): Ate = True #Ate the Apple?
            else:
                save = self.Pos[part].copy()
                self.Pos[part] = temp
            temp = save
        if Ate:
            self.Pos.append(last)
            self.length += 1
            return True, True
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
            if self.Direction_char == 'u': return 20
            if self.Direction_char == 'd': return 21
            if self.Direction_char == 'l': return 22
            if self.Direction_char == 'r': return 23
        elif part == self.length - 1:
            #print("0 pos: " + str(self.Pos[0]))
            #print("1 pos: " + str(self.Pos[1]))

            #print("0 + left pos: " + str(self.Pos[0] + self.Dir_tra['r']))
            if (self.Pos[part] == (self.Pos[part - 1] + self.Dir_tra['u'])).all(): return 31
            if (self.Pos[part] == (self.Pos[part - 1] + self.Dir_tra['d'])).all(): return 30
            if (self.Pos[part] == (self.Pos[part - 1] + self.Dir_tra['l'])).all(): return 33
            if (self.Pos[part] == (self.Pos[part - 1] + self.Dir_tra['r'])).all(): return 32
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
                    '''print ("yes")
                    print(rndPos)'''
                    exist = True
            if exist:
                continue
            break
        #print(" Placed in: " + str(rndPos))
        self.Pos = rndPos

    def get_pos(self):
        return self.Pos[0], self.Pos[1]

class Board():
    def __init__(self, dim):
        # Creating a 2D array represent the snake and the apple
        self.rows, self.columns = dim
        self.board_array = np.full((self.rows, self.columns), 0)
        self.apple = None
        self.E_snake = Snake(self.rows, self.columns)

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
            '''print ("part:" + str(part))
            print("part identity:" + str(self.E_snake.get_part_identity(part)))
            print("part position:" + str(self.E_snake.get_pos_part(part)))'''
            self.board_array[self.E_snake.get_pos_part(part)] = self.E_snake.get_part_identity(part)

        if self.apple != None: # Writes 1 on the board on the position of the apple
            self.board_array[self.apple.get_pos()] = 1
    def step(self, Apple):
        return self.E_snake.step(Apple)

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
    # Updating the board on PyGame
    board_surface = pg.Surface(((b_width * block_s), (b_height * block_s)), pg.SRCALPHA).convert_alpha()
    for c in range(0, b_width):
        for r in range(0, b_height):
            x_o = c * block_s
            y_o = r * block_s
            if board_local[r,c] != 0:
                #print ("HI" + str(board_local[x,y]))
                image = Snake_images[int(convert_images[str(board_local[r,c])])]
                board_surface.blit(image, (x_o, y_o))
    return board_surface

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

def QUIT_snake():
    pg.quit()
    sys.exit()

def show_menu(hover_start, hover_AI, hover_exit):
    global start_rect, AI_rect, exit_rect
    welcome_surface = game_font.render('Welcome to PySnakeAI',True,(255,255,255))
    welcome_rect = welcome_surface.get_rect(center = (pixel_width // 2,pixel_height // 4))
    screen.blit(welcome_surface, welcome_rect)
    start_surface = game_font.render('Single Player Start', True, hovers)
    start_rect = start_surface.get_rect(center=(pixel_width // 2, pixel_height // 4 + 100))
    screen.blit(start_surface, start_rect)
    AI_surface = game_font.render('AI play', True, hoverA)
    AI_rect = AI_surface.get_rect(center=(pixel_width // 2, pixel_height // 4 + 150))
    screen.blit(AI_surface, AI_rect)
    exit_surface = game_font.render('Exit', True, hovere)
    exit_rect = exit_surface.get_rect(center=(pixel_width // 2, pixel_height // 4 + 200))
    screen.blit(exit_surface, exit_rect)

def show_gameover(score):
    global menu_rect
    gameover_surface = game_font.render('GameOver!', True, (200, 200, 200))
    gameover_rect = gameover_surface.get_rect(center = (pixel_width // 2, pixel_height // 4))
    screen.blit(gameover_surface, gameover_rect)

    score_surface = game_font.render(f'Score: {int(score)}' ,True,(200, 200, 200))
    score_rect = score_surface.get_rect(center = (pixel_width // 2, pixel_height // 4 + 100))
    screen.blit(score_surface,score_rect)

    menu_surface = game_font.render('Menu' ,True,hoverm)
    menu_rect = menu_surface.get_rect(center = (pixel_width // 2, pixel_height // 4 + 150))
    screen.blit(menu_surface,menu_rect)




'''PyGame LOOP'''

score = 0
bg_surface = Create_BG(background_images, background_ratios)
E_board = Board((b_height, b_width))
gameStatus = 'menu'# options - menu, game, gameover
gameActive = False
MakeStep = False
while True:
    step = False
    Ate = False

    ''' Games Status Handler'''
    board_surface = Draw_Board(E_board.get_board_array())
    screen.blit(bg_surface, (0,0))
    if gameStatus == 'gameover': show_gameover(score)
    elif gameStatus == 'menu': show_menu(hovers, hoverA, hovere)

    '''END'''
    ''' Event Handler'''
    for event in pg.event.get():
        if event.type == pg.QUIT:
            QUIT_snake()
        if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            QUIT_snake()
        mousePos = pg.mouse.get_pos()
        if gameStatus == 'game':
            if event.type == pg.KEYDOWN:
                if event.key == pygame.K_UP:
                    E_board.C_dir('u')
                    step = True
                if event.key == pg.K_DOWN:
                    E_board.C_dir('d')
                    step = True
                if event.key == pg.K_RIGHT:
                    E_board.C_dir('r')
                    step = True
                if event.key == pg.K_LEFT:
                    E_board.C_dir('l')
                    step = True
            # Single Player Mode
            if E_board.get_apple_exist() == False:
                E_board.Grow_Apple()
            if event.type == STEPEVENT:
                gameActive, Ate = E_board.step(E_board.get_apple_pos())
                step = False
            if not gameActive:
                gameStatus = 'gameover'
                ticking = TICKING_menus
            if Ate:
                E_board.Ate_T_Apple()
                score += 1
            E_board.update_board()

        elif gameStatus == 'gameover':
            #show_gameover(score)
            if menu_rect.collidepoint(mousePos):
                # Handle the Menu button
                hoverm = (150, 150, 150)
            else:
                hoverm = (200, 200, 200)
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                if menu_rect.collidepoint(mousePos):
                    gameStatus = 'menu'

        elif gameStatus == 'menu':
            #show_menu(hovers, hoverA, hovere)
            # Handle the menu mode
            if exit_rect.collidepoint(mousePos):
                # Handle the Exit button
                hovere = (150, 150, 150)
            else:
                hovere = (200, 200, 200)
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                if exit_rect.collidepoint(mousePos):
                    QUIT_snake()

            if start_rect.collidepoint(mousePos):
                # Handle the Start Button
                hovers = (150, 150, 150)
            else:
                hovers = (200, 200, 200)
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                if start_rect.collidepoint(mousePos):
                    gameStatus = 'game'
                    gameActive = True
                    ticking = TICKING_game
                    score = 0
                    E_board = Board((b_height, b_width))

            if AI_rect.collidepoint(mousePos):
                # Handle the AI button
                hoverA = (150, 150, 150)
            else:
                hoverA = (200, 200, 200)
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                if AI_rect.collidepoint(mousePos):
                    QUIT_snake()

    '''END'''

    screen.blit(board_surface, (0, 0))
    pg.display.update()
    clock.tick(ticking)