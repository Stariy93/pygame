import pygame

class Panel():
    def __init__(self, x = 0, y = 0, width = 200, height = 200, color = (61, 109, 161)):
        self.screen = pygame.display.get_surface()
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.rect = pygame.FRect(self.x, self.y, self.width, self.height)
        self.color = color

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def set_position(self, pos = "center", x = 0, y = 0):
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
       
    
        
