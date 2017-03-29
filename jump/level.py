from player import Player
from entity import Entity
import pygame

class Level:
    def __init__(self, n):
        #Attributes
        self.list = [
            Player()
        ]

    def get(self):
        return self.list
