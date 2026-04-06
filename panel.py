import pygame

class Panel():
    def __init__(self, x = 0, y = 0, width = 200, height = 200):
        self.screen = pygame.display.get_surface()
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.rect = pygame.FRect(self.x, self.y, self.width, self.height)

    def draw(self):
        pygame.draw.rect(self.screen, "green", self.rect)
    
        
