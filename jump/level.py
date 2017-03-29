from player import Player
from entity import Entity
import pygame

class Level:
    def __init__(self, n):

        print("New class Level")

        #Attributes
        self.list = [
            Player()
        ]

    def get(self):
        return self.list
