import pygame
from board import Board

class GameOfLife:

    # Constants
    COLUMNS = 100
    ROWS = 200
    TICK_LENGTH = 5000

    # Constructor
    def __init__(self):

        pygame.init()

        # Create Window
        width = self.COLUMNS*Cell.get_width()
        height = self.ROWS*Cell.get_width()
        self.window = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()

        # Create Board
        self.board = Board()

    # Main game loop
    def game(self):
        while True:

            # Handle events
            for event in pygame.event.get():

                # Exit if escape is pressed
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return

            # Black Fill
            self.window.fill((0, 0, 0))

            # Update and Draw board
            self.board.update()
            self.board.draw()

            # Refresh Display
            pygame.display.flip()
            self.clock.tick(60)

            # Wait between each tick
            pygame.time.wait(self.TICK_LENGTH)


# Main entry point
if __name__ == '__main__':
    game_of_life = GameOfLife()
    game_of_life.game()