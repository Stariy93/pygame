import pygame

class Text():
    def __init__(self, font_size = 36, text = ''):
        self.screen = pygame.display.get_surface()
        self.font = pygame.font.Font(None, font_size)
        self.text_surface = self.font.render(text, True, "black")
        self.rect = self.text_surface.get_rect()
        

    def draw(self):
        self.screen.blit(self.text_surface, self.rect)

    def set_position(self, pos = "center", x = 0, y = 0):
        if pos == "center":
            self.rect = self.text_surface.get_rect(center = (x, y))
        elif pos == "left":
            self.rect = self.text_surface.get_rect(topleft = (x, y))
        elif pos == "right":
            self.rect = self.text_surface.get_rect(topright = (x, y))
        elif pos == "top":
            self.rect = self.text_surface.get_rect(midtop = (x, y))
        elif pos == "bottom":
            self.rect = self.text_surface.get_rect(midbottom = (x, y))     