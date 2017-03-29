from level import Level
from inputs import EventHandler
import pygame

MAX_FPS = 30
WINDOW_W = 500
WINDOW_H = 500

class Game:
    def __init__(self):
        #Attributes
        self.stillRunning = True
        self.inputs = None

        #Init modules
        pygame.init()

        clk = pygame.time.Clock()
        screen = pygame.display.set_mode((WINDOW_W, WINDOW_H), pygame.DOUBLEBUF)
        eh = EventHandler()
        pastDelay = 0

        #Load level
        lvl = Level(0)

        #Main loop
        while self.stillRunning:
            #Mange inputs
            self.inputs = eh.getInputs()
            self.handleInputs()

            #Update entities
            for entity in lvl.get():
                entity.update(self.inputs, pastDelay)

            #Render entities
            for entity in lvl.get():
                entity.draw(screen)

            #Display the stuff and wait
            pygame.display.flip()
            pastDelay = clk.tick(MAX_FPS)
            pygame.display.set_caption("fps: " + str(clk.get_fps()))

        #Quit all
        pygame.quit()

    def handleInputs(self):
        if self.inputs[0]['quit'] == True:
            self.stillRunning = False
