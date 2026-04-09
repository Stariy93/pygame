import pygame

class Button_i():
    def __init__(self, file_path = "sprites/sprite_1.png", x = 0, y = 0, text = "start", action=None):
        self.screen = pygame.display.get_surface()
        self.image = pygame.image.load(file_path).convert_alpha()
        self.rect = self.image.get_rect(topleft = (x, y))
        font_size = self.rect.height//2
        self.font = pygame.font.Font(None, font_size)
        
        self.text_surface = self.font.render(text, True, "black")
        self.text_rect = self.text_surface.get_rect(center = self.rect.center)
        self.is_pressed = False
        self.action = action

    def draw(self):
        if self.is_pressed == False:
            self.screen.blit(self.image, self.rect)
        else:
            self.screen.blit(self.image, self.rect)
            pygame.draw.rect(self.screen, "grey", self.rect, 15)
        self.screen.blit(self.text_surface, self.text_rect)

    def event(self, event):
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
        self.text_rect = self.text_surface.get_rect(center = self.rect.center)

