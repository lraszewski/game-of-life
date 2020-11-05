import pygame
import random
from cell import Cell

class Board:

    # Constructor
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.grid = [[Cell(column*Cell.get_width(), row*Cell.get_width()) for column in range(self.columns)] for row in range(self.rows)]
        self.generate_random()

    # Generate states of the cells randomly
    def generate_random(self):
        for row in range(self.rows):
            for column in range(self.columns):
                chance = random.randint(0, 1)
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
                elif (neighbour_row < 0) or (neighbour_row >= self.rows):
                    valid = False
                elif (neighbour_column < 0) or (neighbour_column >= self.columns):
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

        for row in range(self.rows):
            for column in range(self.columns):

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
        for row in range(self.rows):
            for column in range(self.columns):
                cell = self.grid[row][column]
                cell.draw(window)
