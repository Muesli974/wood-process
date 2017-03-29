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



class lightEffect(object):
    """docstring for lightEffect."""
    def __init__(self, lightType, position = (0, 0)):
        self.sheet = pygame.image.load(lightImageMapper(lightType))
        self.x = position[0]
        self.y = position[1]
        self.lightType = lightType

    def update(self, inputs):
        (self.x, self.y) = map(lambda x: x-self.lightType/2, pygame.mouse.get_pos())
    def draw(self, shadow):
        shadow.blit(self.sheet, (self.x, self.y))
