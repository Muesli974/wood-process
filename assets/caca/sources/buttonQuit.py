import button

class buttonQuit(button):
    """docstring for buttonQuit."""
    def __init__(self, caption = "Quit", font = "monospace"):
        button.__init__()
        self.text = caption
        self.font = pygame.font.SysFont(font, 15)

    def draw(self, screen, position):
        button.draw(screen, position)
        screen.blit(self.font.render(self.text, 1, (0, 0, 0)), position)

    def activate(self, launcher):
        launcher.quit()
