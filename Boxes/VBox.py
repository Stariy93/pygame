import pygame

class VBox():
    def __init__(self, pos = "center", rect = None, gap = 10, padding = 10):
        self.pos = pos
        if rect is None:
            surface = pygame.display.get_surface()
            if surface is None:
                raise ValueError("VBox rect is required before the display surface is created")
            rect = surface.get_rect()
        self.rect = rect
        self.gap = gap
        self.padding = padding
        self.children = []

    def add(self, widget):
        self.children.append(widget)

    def apply(self):           
        if self.pos == "center":
            y = self.rect.top + self.padding
            pos_x = self.rect.centerx    

        elif self.pos == "left":
            y = self.rect.top + self.padding
            pos_x = self.rect.left + self.gap

        elif self.pos == "right":
            y = self.rect.top + self.padding
            pos_x = self.rect.right - self.gap

        for widget in self.children:
            if self.pos == "center":
                widget.set_position(self.pos, pos_x, y + widget.rect.height // 2)
            else:
                widget.set_position(self.pos, pos_x, y)
            y += widget.rect.height + self.gap

