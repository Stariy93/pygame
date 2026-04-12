import pygame

class Spacer:
    def __init__(self, width=0, height=0):
        self.rect = pygame.FRect(0, 0, width, height)

    def draw(self):
        pass

    def event(self, event):
        pass

    def set_position(self, pos="center", x=0, y=0):
        if pos == "center":
            self.rect.center = (x, y)
        elif pos == "left":
            self.rect.topleft = (x, y)
        elif pos == "right":
            self.rect.topright = (x, y)
        elif pos == "top":
            self.rect.midtop = (x, y)
        elif pos == "bottom":
            self.rect.midbottom = (x, y)