import pygame
import sys
from board import Board
from cell import Cell

class GameOfLife:

    # Constants
    COLUMNS = 100
    ROWS = 100
    TICK_LENGTH = 100

    # Constructor
    def __init__(self):

        # Initialise pygame
        pygame.init()
        pygame.display.set_caption('The Game of Life')

        # Create Window
        width = self.COLUMNS*Cell.get_width()
        height = self.ROWS*Cell.get_width()
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_icon(self.window)
        self.clock = pygame.time.Clock()

        # Create Board
        self.board = Board(self.ROWS, self.COLUMNS)

    # Main game loop
    def game(self):
        while True:

            # Handle events
            for event in pygame.event.get():

                # Exit if a quit action has been taken
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Exit if escape is pressed
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            # Black Fill
            self.window.fill((0, 0, 0))

            # Update and Draw board
            self.board.update()
            self.board.draw(self.window)

            # Refresh Display
            pygame.display.flip()
            self.clock.tick(60)

            # Wait between each tick
            pygame.time.wait(self.TICK_LENGTH)


# Main entry point
if __name__ == '__main__':
    game_of_life = GameOfLife()
    game_of_life.game()