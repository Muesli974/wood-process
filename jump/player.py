from entity import Entity
import pygame

PLAYER_W = 64
PLAYER_H = 64
PLAYER_IMG = pygame.image.load("../assets/circle_sheet.png")
PLAYER_SEQ = (4, 2, 0, 0, PLAYER_W, PLAYER_H)

class Player(Entity):
    def __init__(self):
        print("New class Player")
        #Attributes
        Entity.__init__(self, PLAYER_W, PLAYER_H)
        self.animate(PLAYER_IMG, PLAYER_SEQ)

    def update(self, inputs):
        pass

    def draw(self, screen):
        Entity.draw(self, screen)
