import pygame
from buttonQuit import buttonQuit
from buttonStart import buttonStart

class launcher(object):
    """docstring for launcher."""
    title = "Game Launcher"
    background = pygame.image.load("../assets/bgLauncher.png")
    icon = pygame.image.load("../assets/iconLauncher.png")
    stillRunning = True

    buttons = []

    def __init__(self, size = (800, 600)):
        # Create the window
        self.size = size
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode(self.size, pygame.DOUBLEBUF)
        pygame.display.set_caption(self.title)
        pygame.display.set_icon(self.icon)

        # init Font
        pygame.font.init()

        # Set the background
        self.window.blit(self.background, (0, 0))

        # create some buttons
        self.buttons.append(buttonStart((100, 100)))
        self.buttons.append(buttonQuit((100, 175)))

        while self.stillRunning:
            # events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.stillRunning = False
            for button in self.buttons:
                button.update(self)
                button.draw(self.window)
            #display
            pygame.display.flip()
            self.clock.tick(60)
        #Quit all
        pygame.quit()

    def __del__(self):
        pass

    def quit(self):
        self.stillRunning = False
