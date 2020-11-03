import pygame
from cell import Cell

class Board:

    # Constants
    ROWS = 100
    COLUMNS = 200

    # Constructor
    def __init__(self):
        self.grid = [[Cell() for column in range(self.COLUMNS)] for row in range(self.ROWS)]
        self.generate_random()

    # Generate states of the cells randomly
    def generate_random(self):
        for row in range(self.ROWS):
            for column in range(self.COLUMNS):
                chance = randint(0, 1):
                if chance == 1:
                    cell = self.grid[row][column]
                    cell.revive()

    # Get valid neighbours of a given cell
    def get_neighbours(self, check_row, check_column):

        # How deep is the search
        min = -1
        max = 2

        # Empty list to store neighbours
        neighbours = []
        for row in range(min, max):
            for column in range(min, max):

                neighbour_row = check_row + row
                neighbour_column = check_column + column

                # Check if is a valid neighbour
                valid = True
                if (neighbour_row == check_row) and (neighbour_column == check_column):
                    valid = False
                elif (neighbour_row < 0) or (neighbour_row >= self.ROWS):
                    valid = False
                elif (neighbour_column < 0) or (neighbour_column >= self.COLUMNS):
                    valid = False

                # If neighbour is valid, store it
                if valid:
                    neighbours.append(self.grid[neighbour_row][neighbour_column])

        # Return list of neighbours
        return neighbours

    # Update the board according to game logic
    def update(self):

        # Store cells we need to revive, and those we need to kill
        revive = []
        kill = []

        for row in range(self.ROWS):
            for column in range(self.COLUMNS):

                # Get Neighbours
                neighbours = self.get_neighbours(row, column)
                
                # Find out which ones are alive
                living = []
                for cell in neighbours:
                    if cell.is_alive():
                        living.append(cell)
                
                # Get the cell
                cell = self.grid[row][column]

                # Any live cell without two or three live neighbours dies
                if cell.is_alive():
                    if len(living) > 3 or len(living) < 2:
                        kill.append(cell)

                # Any dead cell with three live neighbours becomes a live cell
                else:
                    if len(living) == 3:
                        revive.append(cell)

        # Revive cells
        for cell in revive:
            cell.revive()
        
        # Kill cells
        for cell in kill:
            cell.kill()

    # Draw Board
    def draw(self, window):
        for row in range(self.ROWS):
            for column in range(self.COLUMNS):
                cell = self.grid[row][cell]
                cell.draw(window)
