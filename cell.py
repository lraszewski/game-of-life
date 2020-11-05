import pygame
from status import Status

class Cell(pygame.Rect):

    # Constants
    WIDTH = 10
    COLOUR = (255, 255, 255)

    # Initialise cell as dead
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.status = Status.DEAD
        super().__init__(x, y, self.WIDTH, self.WIDTH)

    # Set the status of the cell to dead
    def kill(self):
        self.status = Status.DEAD

    # Set the status of the cell to alive
    def revive(self):
        self.status = Status.ALIVE

    # Check if the cell is alive
    def is_alive(self):
        if self.status == Status.ALIVE:
            return True
        return False

    # Draw the cell
    def draw(self, window):
        if self.is_alive():
            pygame.draw.rect(window, self.COLOUR, self)

    # Get the cell width
    def get_width():
        return Cell.WIDTH