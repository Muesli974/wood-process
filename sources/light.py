import pygame, layer

def lightImageMapper(arg):
    switcher= {
        50: "../assets/light50.png",
        100: "../assets/light100.png",
        150: "../assets/light150.png",
        200: "../assets/light200.png",
    }
    # light100 is returned by default if
    return switcher.get(arg, "../assets/light100.png")



class lightEffect(layer.Layer):
    """docstring for lightEffect."""
    def __init__(self, type):

        super(lightEffect, self).__init__(lightImageMapper(type))
        self.type = type
        self.x = type/2
        self.y = type/2

    def update(self, inputs):
        (self.x, self.y) = pygame.mouse.get_pos()
    def draw(self, filter):
        filter.blit(self.sheet, (100, 100), None)
