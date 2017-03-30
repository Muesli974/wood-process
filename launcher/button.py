import pygame
from abc import ABCMeta, abstractmethod

class button(metaclass=ABCMeta):
    """docstring for button."""
    image = pygame.image.load("../assets/buttonLauncher.png")
    imagePeaked = pygame.image.load("../assets/buttonLauncherPeaked.png")

    def __init__(self, position):
        self.isPeaked = False
        self.position = position
        self.text = ""
    def isMouseOn(self):
        mousePos = pygame.mouse.get_pos()
        x = -self.position[0] + mousePos[0]
        y = -self.position[1] + mousePos[1]
        return self.image.get_bounding_rect().collidepoint((x, y))

    def update(self, launcher):
        if(self.isMouseOn()):
            self.isPeaked = True
            if(pygame.mouse.get_pressed()[0]):
                self.activate(launcher)
        else:
            self.isPeaked = False

    def draw(self, screen):
        if(self.isPeaked):
            image = self.imagePeaked
        else:
            image = self.image
        font = self.font.render(self.text, 1, (0, 0, 0))
        image.blit(font, (80, 20))
        screen.blit(image, self.position)


    def activate(self, launcher):
        # to overwrite in subclass
        pass
