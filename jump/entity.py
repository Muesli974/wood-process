from animation import Animation
import pygame

DRAW_COLOR = (100, 100, 100)

class Entity:
    def __init__(self, w, h, x = 0.0, y = 0.0):
        print("New class Entity")
        #Attributes
        self.w = w
        self.h = h
        self.x = x
        self.y = y
        self.anim = None

    def update(self, inputs):
        pass

    def draw(self, screen):
        x = int(self.x)
        y = int(self.y)
        if self.anim != None:
            self.anim.draw(screen, (x, y))
        else:
            pygame.draw.rect(screen, DRAW_COLOR, pygame.Rect(x, y, w, h))

    def animate(self, sheet, seq):
        self.anim = Animation(sheet, seq)
