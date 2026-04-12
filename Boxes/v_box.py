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

    def get_content_size(self):
        if not self.children:
            return self.padding * 2, self.padding * 2

        total_height = self.padding * 2 + sum(widget.rect.height for widget in self.children)
        total_height += self.gap * max(0, len(self.children) - 1)
        content_width = self.padding * 2 + max(widget.rect.width for widget in self.children)
        return content_width, total_height

    def apply(self, rect = None, offset_x = 0, offset_y = 0):
        if rect is None:
            rect = self.rect
        self.rect = rect

        if self.pos == "center":
            y = self.rect.top + self.padding - offset_y
            pos_x = self.rect.centerx - offset_x

        elif self.pos == "left":
            y = self.rect.top + self.padding - offset_y
            pos_x = self.rect.left + self.gap - offset_x

        elif self.pos == "right":
            y = self.rect.top + self.padding - offset_y
            pos_x = self.rect.right - self.gap - offset_x

        else:
            raise ValueError("VBox pos must be 'left', 'center' or 'right'")

        for widget in self.children:
            if self.pos == "center":
                widget.set_position(self.pos, pos_x, y + widget.rect.height // 2)
            else:
                widget.set_position(self.pos, pos_x, y)
            y += widget.rect.height + self.gap

    def draw(self):
        for cild in self.children:
            cild.draw()
    
    def event(self, event):
        for cild in self.children:
            cild.event(event)
