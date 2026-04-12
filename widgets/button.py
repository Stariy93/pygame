import pygame
from widgets.widget import Widget

class Button(Widget):
    def __init__(self, x = 0, y = 0, font_size = 30, text = "", action=None):
        super().__init__()
        self.font = pygame.font.Font(None, font_size)
        self.text_surface = self.font.render(text, True, "black")
        self.rect_width = (self.text_surface.get_width()) + font_size * 2
        self.rect_height = font_size * 3
        self.rect = pygame.FRect(x - self.rect_width//2, y - self.rect_height//2, self.rect_width, self.rect_height)
        self.text_rect = self.text_surface.get_rect(center = self.rect.center)
        self.is_pressed = False
        self.action = action

    def _draw(self):
        if self.is_pressed == False:
            pygame.draw.rect(self.screen, "grey", self.rect, 5)
        else:
            pygame.draw.rect(self.screen, "grey", self.rect, 15)
        self.screen.blit(self.text_surface, self.text_rect)

    def _event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.is_pressed = True

                
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.is_pressed = True
                if self.action is not None:
                    self.action()
            self.is_pressed = False
            
    def set_position(self, pos = "center", x = 0, y = 0):
        super().set_position(pos, x, y)
        self.text_rect = self.text_surface.get_rect(center = self.rect.center)






