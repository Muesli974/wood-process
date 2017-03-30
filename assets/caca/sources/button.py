import pygame
from abc import ABCMeta, abstractmethod

class button(pygame.Surface, metaClass=ABCMeta):
    """docstring for button."""
    image = pygame.image.load("../assets/buttonLauncher.png")
    imagePeaked = pygame.image.load("../assets/buttonLauncherPeaked.png")

    def __init__(self):
        self.peaked = False
    def isMouseOn(self):
         return self.get_bounding_rect().collidepoint(pygame.mouse.get_pos())

    def update(self):
        if(self.isMouseOn()):
            self.peaked = True
            if(pygame.mouse.get_pressed()[0]):
                self.activate()
        else:
            self.peaked = False

    def draw(self, screen, position):
        if(self.peaked):
            screen.blit(self.imagePeaked, position)
        else:
            screen.blit(self.image, position)



    def activate(self):
        # to overwrite in subclass
        pass
