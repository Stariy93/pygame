import pygame

class HBox():
    def __init__(self, pos = "center", rect = None, gap = 10, padding = 10):
        self.pos = pos
        if rect is None:
            surface = pygame.display.get_surface()
            if surface is None:
                raise ValueError("HBox rect is required before the display surface is created")
            rect = surface.get_rect()
        self.rect = rect
        self.gap = gap
        self.padding = padding
        self.children = []

    def add(self, widget):
        self.children.append(widget)

    def apply(self):           
        if self.pos == "center":
            x = self.rect.left + self.padding
            pos_y = self.rect.centery

        elif self.pos == "top":
            x = self.rect.left + self.padding
            pos_y = self.rect.top + self.gap

        elif self.pos == "bottom":
            x = self.rect.left + self.padding
            pos_y = self.rect.bottom - self.gap

        else:
            raise ValueError("HBox pos must be 'top', 'center' or 'bottom'")

        for widget in self.children:
            if self.pos == "center":
                widget.set_position(self.pos, x + widget.rect.width // 2, pos_y)
            else:
                widget.set_position(self.pos, x + widget.rect.width // 2, pos_y)
            x += widget.rect.width + self.gap