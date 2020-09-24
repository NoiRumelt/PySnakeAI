import numpy as np
import tensorflow.

class Snake():
    def __init__(self, col,row):
        self.Pos = [np.array([row // 2, col // 2])]
        self.Direction = np.array([-1,0]) # The options are: 'u' - Up, 'd' - Down, 'l' - Left, 'r' - Right
        self.length = 1
    def __repr__(self):
        return Pos
    def step(self):
        # No Input, taking the current position of the snake and the current direction of it, and change the 2D array,
        # moving the snake 1 step ahead, drawing the new head, deleting the the tail. not checking for collisions.
        # updating the snake length.
        for part in range(0, len(self.Pos)):
            if part == 0:
                save = self.Pos[part]
                self.Pos[0] += self.Direction
            else:
                save = self.Pos[part]
                self.Pos[part] = temp
            temp = save

    def C_dir(self, dir):
        # Changing the direction of the moving of the snake
        if dir == 'u': self.Direction = np.array([-1, 0])
        if dir == 'd': self.Direction = np.array([1, 0])
        if dir == 'l': self.Direction = np.array([0, -1])
        if dir == 'r': self.Direction = np.array([0, 1])
    def Ate_T_Apple(self):
        # Starting when the pygame says we hit the apple, it making a step at the direction we currently hold, without
        # "deleting" the tail, means it only moves the head and not the tail.
        pass

s = Snake(10,10)
s.step()
s.step()
s.C_dir('r')
s.step()
print(s.Pos)