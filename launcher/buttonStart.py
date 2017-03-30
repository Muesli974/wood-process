import pygame
from button import button
#from GameHandler import GameHandler

class buttonStart(button):
    """docstring for buttonStart."""
    def __init__(self, position, caption="Start", font="Arial"):
        button.__init__(self, position)
        self.text = caption
        self.font = pygame.font.SysFont(font, 25)

    def activate(self, launcher):
        #GameHandler()
        pass
