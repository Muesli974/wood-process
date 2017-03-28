import pygame, layer, light

class Game:
    fps = 60
    isRunning = True

    # All the shit to display
    layers = []
    effects = []
    # inputs listeners
    inputs = {
        "left": False,
        "up": False,
        "right": False,
        "down": False
    }

    def __init__(self):
        # Launch pygame modules
        pygame.display.init()

        # Create the window
        self.window = Window()

        # Create the clock
        self.clock = pygame.time.Clock()

        # shadow init
        self.shadow = pygame.surface.Surface(self.window.size)
        self.shadow.fill(pygame.color.Color('Grey'))

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

            # Events handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.end()
                elif event.type == pygame.KEYDOWN:
                    self.onKeyDown(event.key)
                elif event.type == pygame.KEYUP:
                    self.onKeyUp(event.key)

            # Update and draw all the shit
            for layer in self.layers:
                layer.update(self.inputs)
                layer.draw(self.window.win)
            for effect in self.effects:
                effect.update(self.inputs)
                effect.draw(self.shadow)

            self.shadow.blit(self.shadow, (0, 0), special_flags= pygame.BLEND_RGBA_SUB)

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
