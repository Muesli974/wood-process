import pygame

class Animation:
    def __init__(self, sheet, seq):
        #Attributes

        print("New class Animation")

        self.sheet = sheet
        self.length = seq[0]
        self.delay = seq[1]
        self.x = seq[2]
        self.y = seq[3]
        self.w = seq[4]
        self.h = seq[5]
        self.step = 0
        self.tick = 0
        self.curX = self.x

    def draw(self, screen, dest):
        screen.blit(self.sheet, dest, pygame.Rect(self.curX, self.y, self.w, self.h))
        if self.tick == self.delay:
            self.tick = 0

            self.step += 1
            if self.step < self.length:
                self.curX += self.w
            else:
                self.step = 0
                self.curX = self.x
        else:
            self.tick += 1
