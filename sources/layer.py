import pygame

class Layer:
    def __init__(self, sheetName, position = (0, 0)):
        self.sheet = pygame.image.load(sheetName)
        self.x = position[0]
        self.y = position[1]
        self.vx = 0
        self.vy = 0

    def update(self, inputs):
        if inputs["left"] == True:
            self.vx -= 2
        if inputs["up"] == True:
            self.vy -= 2
        if inputs["right"] == True:
            self.vx += 2
        if inputs["down"] == True:
            self.vy += 2

        self.x += self.vx
        self.y += self.vy

        self.vx *= 0.95
        self.vy *= 0.95

    def draw(self, screen):
        screen.blit(self.sheet, (self.x, self.y), None)

class Entity(Layer):
    def __init__(self, sheetName, position = (0, 0)):
        Layer.__init__(sheetName, position)
