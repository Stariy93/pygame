import pygame
from widgets.widget import Widget

class Image(Widget):
    def __init__(self,file_path = None, x = 0, y = 0):
        super().__init__()
        self.image = pygame.image.load(file_path).convert_alpha()
        self.rect = self.image.get_rect(topleft = (x, y))

    def _draw(self):
        self.screen.blit(self.image, self.rect)
