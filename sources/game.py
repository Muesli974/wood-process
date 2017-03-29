import pygame, layer, light, keyboard

class Game:
    fps = 60
    isRunning = True

    # All the shit to display
    layers = []
    effects = []


    def __init__(self):
        # Launch pygame modules
        pygame.display.init()

        # Create the window
        self.window = Window()

        # Create the clock
        self.clock = pygame.time.Clock()

        # Create the keyboard handler
        self.keyboard = keyboard.keyboard()

        # Create some layers
        self.layers.append(layer.Layer("../assets/circle.png"))
        self.effects.append(light.lightEffect(100))

    def __del__(self):
        pass

    def start(self):
        # Start the main loop
        while self.isRunning:
            # Time manager
            self.clock.tick(self.fps)

            # Update the inputs
            self.keyboard.update()

            # shadow init
            shadow = pygame.surface.Surface((1920,1080))
            shadow.fill(pygame.color.Color('Grey'))

            # Update and draw all the shit
            for layer in self.layers:
                layer.update(self.keyboard.inputs)
                layer.draw(self.window.win)
            for effect in self.effects:
                effect.update(self.keyboard.inputs)
                effect.draw(shadow)

            self.window.win.blit(shadow, (0, 0), special_flags= pygame.BLEND_RGBA_SUB)

            # Flip the screen
            pygame.display.flip()

        # Delete the Window
        del self.window

        # Quit all pygame modules
        # The pygame window will be deleted at this time
        pygame.display.quit()

    def end(self):
        # Close the main loop
        self.isRunning = False

class Window:
    title = "Suce ma bite!"
    size = (0, 0)
    bgColor = (35, 35, 255)

    def __init__(self):
        # Create the window
        self.win = pygame.display.set_mode(self.size, pygame.DOUBLEBUF)

        # Fill the background and set the title
        self.win.fill(self.bgColor)
        pygame.display.set_caption(self.title)

    def __del__(self):
        pass
