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

    def get_content_size(self):
        if not self.children:
            return self.padding * 2, self.padding * 2

        total_width = self.padding * 2 + sum(widget.rect.width for widget in self.children)
        total_width += self.gap * max(0, len(self.children) - 1)
        content_height = self.padding * 2 + max(widget.rect.height for widget in self.children)
        return total_width, content_height

    def apply(self, rect = None, offset_x = 0, offset_y = 0):
        if rect is None:
            rect = self.rect
        self.rect = rect

        if self.pos == "center":
            x = self.rect.left + self.padding - offset_x
            pos_y = self.rect.centery - offset_y

        elif self.pos == "top":
            x = self.rect.left + self.padding - offset_x
            pos_y = self.rect.top + self.gap - offset_y

        elif self.pos == "bottom":
            x = self.rect.left + self.padding - offset_x
            pos_y = self.rect.bottom - self.gap - offset_y

        else:
            raise ValueError("HBox pos must be 'top', 'center' or 'bottom'")

        for widget in self.children:
            if self.pos == "center":
                widget.set_position(self.pos, x + widget.rect.width // 2, pos_y)
            else:
                widget.set_position(self.pos, x + widget.rect.width // 2, pos_y)
            x += widget.rect.width + self.gap

    def draw(self):
        for cild in self.children:
            cild.draw()
    
    def event(self, event):
        for cild in self.children:
            cild.event(event)