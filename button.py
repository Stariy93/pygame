import pygame

class Button():
    def __init__(self, x, y, font_size, text, action=None):
        self.screen = pygame.display.get_surface()
        self.font = pygame.font.Font(None, font_size)
        self.text_surface = self.font.render(text, True, "black")
        self.rect_width = (self.text_surface.get_width()) + font_size * 2
        self.rect_height = font_size * 3
        self.rect = pygame.FRect(x - self.rect_width//2, y - self.rect_height//2, self.rect_width, self.rect_height)
        self.text_rect = self.text_surface.get_rect(center = self.rect.center)
        self.mouse_tup = False
        self.action = action
    def draw(self):
        if self.mouse_tup == False:
            pygame.draw.rect(self.screen, "grey", self.rect, 5)
        else:
            pygame.draw.rect(self.screen, "grey", self.rect, 15)
        self.screen.blit(self.text_surface, self.text_rect)

    def event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.mouse_tup = True
                if self.action is not None:
                    self.action()
                
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.mouse_tup = False
            



