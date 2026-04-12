import pygame


class Widget:
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.rect = pygame.FRect(0, 0, 0, 0)
        self.visible = True
        self.enabled = True

    def show(self):
        self.visible = True
        return self

    def hide(self):
        self.visible = False
        return self

    def enable(self):
        self.enabled = True
        return self

    def disable(self):
        self.enabled = False
        return self

    def draw(self):
        if not self.visible:
            return
        self._draw()

    def _draw(self):
        raise NotImplementedError

    def event(self, event):
        if not self.visible or not self.enabled:
            return
        self._event(event)

    def _event(self, event):
        pass

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