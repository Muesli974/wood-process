from entity import Entity
import pygame

PLAYER_W = 64
PLAYER_H = 64
PLAYER_IMG = pygame.image.load("../assets/circle_sheet.png")
PLAYER_SEQ = (4, 2, 0, 0, PLAYER_W, PLAYER_H)
PLAYER_INERTIA = 0.95
SPEED_APPLICATION = 0.1

PLAYER_MIN_X = 0.0
PLAYER_MIN_Y = 0.0
PLAYER_MAX_X = float(500.0 - PLAYER_W)
PLAYER_MAX_Y = float(500.0 - PLAYER_H)

class Player(Entity):
    def __init__(self, id):
        #Attributes
        Entity.__init__(self, PLAYER_W, PLAYER_H)
        self.vx = 0.0
        self.vy = 0.0
        self.id = id

        #Set animation
        self.animate(PLAYER_IMG, PLAYER_SEQ)

    def update(self, inputs, pastDelay):
        #Update speed
        self.vx += inputs[self.id]['axisX'] * pastDelay
        self.vy += inputs[self.id]['axisY'] * pastDelay
        self.vx *= PLAYER_INERTIA
        self.vy *= PLAYER_INERTIA

        #Update coordinates
        self.x += self.vx * SPEED_APPLICATION
        self.y += self.vy * SPEED_APPLICATION

        #Check for out of bounds position
        if self.x < PLAYER_MIN_X:
            self.x = PLAYER_MIN_X + (PLAYER_MIN_X - self.x)
            self.vx = -self.vx
        elif self.x > PLAYER_MAX_X:
            self.x = PLAYER_MAX_X - (self.x - PLAYER_MAX_X)
            self.vx = -self.vx
        if self.y < PLAYER_MIN_Y:
            self.y = PLAYER_MIN_Y + (PLAYER_MIN_Y - self.y)
            self.vy = -self.vy
        elif self.y > PLAYER_MAX_Y:
            self.y = PLAYER_MAX_Y - (self.y - PLAYER_MAX_Y)
            self.vy = -self.vy


    def draw(self, screen):
        Entity.draw(self, screen)
