import pygame
from button import button

class buttonQuit(button):
    """docstring for buttonQuit."""
    def __init__(self, position, caption="Quit", font="Arial"):
        button.__init__(self, position)
        self.text = caption
        self.font = pygame.font.SysFont(font, 25)

    def activate(self, launcher):
        launcher.quit()
