import pygame

class Mario:
    """Main character in game"""

    def __init__(self, mario_game):
        """initialization main character and its position"""

        self.screen = mario_game.screen
        self.screen_rect = mario_game.screen.get_rect()

        #Load image
        self.image = pygame.image.load('images/mario.png')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom


    def blitme(self):
        """"Displaying Mario at his current position"""
        self.screen.blit(self.image, self.rect)
