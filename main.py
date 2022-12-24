import pygame
import random

width, height = 600, 400

display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Q Learning")


class Environment:
    def __init__(self, grid):
        self.grid = grid
        self.initial_state = None
        self.positive_terminal_state = None   # State with the highest possible "reward" value
        self.negative_terminal_state = None   # State with the lowest possible "reward" value
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    self.initial_state = (r, c)
                
                elif grid[r][c] == 1:
                    self.positive_terminal_state = (r, c)

                elif grid[r][c] == -1:
                    self.negative_terminal_state = (r, c)

                else:
                    # Any 'ol cell, so
                    pass


    def dump(self, verbose = False):
        for row in self.grid:
            print(" ".join(str(i) for i in row))

        if verbose:
            print(f"Initial State : {self.initial_state}")
            print(f"Positive State : {self.positive_terminal_state}")
            print(f"Negative State : {self.negative_terminal_state}")
        

class Agent:
    def __init__(self, environment):
        self.env = environment
        self.current_state = environment.initial_state


def main():
    loop = True

    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
                quit()

        pygame.display.flip()

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 1],
        [0, 0, 0, -1],
        [2, 0, 0, 0]
    ]

    env = Environment(grid)
    env.dump(True)

