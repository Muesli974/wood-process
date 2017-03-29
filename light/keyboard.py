import pygame

class keyboard(object):
    """docstring for keyboard."""
    def __init__(self):
        super(keyboard, self).__init__()
        # inputs listeners
        self.inputs = {
            "left": False,
            "up": False,
            "right": False,
            "down": False
        }

    def update(self, game):
        # Events handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.end()
            elif event.type == pygame.KEYDOWN:
                self.onKeyDown(event.key)
            elif event.type == pygame.KEYUP:
                self.onKeyUp(event.key)
        pass

    def onKeyDown(self, key):
        if key == pygame.K_LEFT:
            self.inputs["left"] = True
        elif key == pygame.K_UP:
            self.inputs["up"] = True
        elif key == pygame.K_RIGHT:
            self.inputs["right"] = True
        elif key == pygame.K_DOWN:
            self.inputs["down"] = True

    def onKeyUp(self, key):
        if key == pygame.K_LEFT:
            self.inputs["left"] = False
        elif key == pygame.K_UP:
            self.inputs["up"] = False
        elif key == pygame.K_RIGHT:
            self.inputs["right"] = False
        elif key == pygame.K_DOWN:
            self.inputs["down"] = False
