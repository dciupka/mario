import sys
import pygame
from settings import Settings
from mario import Mario

class MarioGame:
    """This is my mario game, main class game"""
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Mario Bros')
        self.mario = Mario(self) # musi być po self.screen


    def run_game(self):
        """Main loop game"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.settings.bg_color)
            #Present last modified screen
            self.mario.blitme()

            pygame.display.flip()


if __name__ == '__main__':
    mg = MarioGame()
    mg.run_game()