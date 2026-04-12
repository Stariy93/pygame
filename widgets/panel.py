import pygame
from widgets.widget import Widget
from widgets.slider import Slider

class Panel(Widget):
    def __init__(self, x = 0, y = 0, width = 200, height = 200, color = (60, 110, 160),
                 padding = 12, slider_size = 28, scroll_step = 40, layout = None):
        super().__init__()
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.rect = pygame.FRect(self.x, self.y, self.width, self.height)
        self.color = color
        self.padding = padding
        self.slider_size = slider_size
        self.scroll_step = scroll_step
        self.layout = layout
        self.viewport_rect = pygame.FRect(self.rect)
        self.corner_rect = pygame.FRect(0, 0, 0, 0)
        self.content_size = (0, 0)
        self.max_scroll_x = 0
        self.max_scroll_y = 0
        self.scroll_x = 0
        self.scroll_y = 0
        self.vertical_slider = Slider(
            width = max(1, int(self.rect.height)),
            min_value = 0,
            max_value = 1,
            value = 0,
            step = 1,
            action = self._set_scroll_y,
            orientation = "vertical",
        )
        self.horizontal_slider = Slider(
            width = max(1, int(self.rect.width)),
            min_value = 0,
            max_value = 1,
            value = 0,
            step = 1,
            action = self._set_scroll_x,
        )
        self._refresh_layout()

    def set_position(self, pos = "center", x = 0, y = 0):
        super().set_position(pos, x, y)
        self._refresh_layout()

    def set_layout(self, layout):
        self.layout = layout
        self._refresh_layout()
        return self

    def add(self, widget):
        if self.layout is None:
            raise ValueError("Panel layout must be set before adding widgets")
        self.layout.add(widget)
        self._refresh_layout()
        return self

    def _draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        previous_clip = self.screen.get_clip()
        self.screen.set_clip(self.viewport_rect)

        if self.layout is not None:
            self.layout.draw()

        self.screen.set_clip(previous_clip)

        if self.max_scroll_y > 0:
            self.vertical_slider.draw()
        if self.max_scroll_x > 0:
            self.horizontal_slider.draw()
        if self.max_scroll_x > 0 and self.max_scroll_y > 0:
            pygame.draw.rect(self.screen, "grey20", self.corner_rect)

        pygame.draw.rect(self.screen, "grey20", self.rect, 2)
        pygame.draw.rect(self.screen, "grey10", self.viewport_rect, 1)

    def _event(self, event):
        if self.max_scroll_y > 0:
            self.vertical_slider.event(event)
        if self.max_scroll_x > 0:
            self.horizontal_slider.event(event)

        if event.type == pygame.MOUSEWHEEL:
            if self.viewport_rect.collidepoint(pygame.mouse.get_pos()):
                self._scroll_wheel(event)
            return

        if self.layout is None:
            return

        if hasattr(event, "pos") and not self.viewport_rect.collidepoint(event.pos):
            return

        self.layout.event(event)

    def _refresh_layout(self):
        if self.layout is None:
            self.viewport_rect = pygame.FRect(
                self.rect.left + self.padding,
                self.rect.top + self.padding,
                max(1, self.rect.width - self.padding * 2),
                max(1, self.rect.height - self.padding * 2),
            )
            return

        self.content_size = self.layout.get_content_size()
        self.viewport_rect, show_h, show_v = self._build_viewport_rect()
        self.max_scroll_x = max(0, int(round(self.content_size[0] - self.viewport_rect.width)))
        self.max_scroll_y = max(0, int(round(self.content_size[1] - self.viewport_rect.height)))
        self.scroll_x = min(self.scroll_x, self.max_scroll_x)
        self.scroll_y = min(self.scroll_y, self.max_scroll_y)

        self._update_scrollbars(show_h, show_v)
        self.layout.apply(self.viewport_rect, offset_x = self.scroll_x, offset_y = self.scroll_y)

    def _build_viewport_rect(self):
        left = self.rect.left + self.padding
        top = self.rect.top + self.padding
        available_width = max(1, self.rect.width - self.padding * 2)
        available_height = max(1, self.rect.height - self.padding * 2)

        show_v = self.content_size[1] > available_height
        show_h = self.content_size[0] > available_width

        for _ in range(2):
            viewport_width = max(1, available_width - (self.slider_size if show_v else 0))
            viewport_height = max(1, available_height - (self.slider_size if show_h else 0))
            show_v = self.content_size[1] > viewport_height
            show_h = self.content_size[0] > viewport_width

        viewport_rect = pygame.FRect(left, top, viewport_width, viewport_height)
        return viewport_rect, show_h, show_v

    def _update_scrollbars(self, show_h, show_v):
        self.corner_rect = pygame.FRect(0, 0, 0, 0)

        if show_v:
            self.vertical_slider.set_rect(pygame.FRect(
                self.viewport_rect.right,
                self.viewport_rect.top,
                self.slider_size,
                self.viewport_rect.height,
            ))
            self.vertical_slider.max_value = max(1, self.max_scroll_y)
            self.vertical_slider.step = 1
            self.vertical_slider.enable()
            self.vertical_slider.set_value(self.scroll_y)
        else:
            self.vertical_slider.disable()
            self.vertical_slider.set_value(0)

        if show_h:
            self.horizontal_slider.set_rect(pygame.FRect(
                self.viewport_rect.left,
                self.viewport_rect.bottom,
                self.viewport_rect.width,
                self.slider_size,
            ))
            self.horizontal_slider.max_value = max(1, self.max_scroll_x)
            self.horizontal_slider.step = 1
            self.horizontal_slider.enable()
            self.horizontal_slider.set_value(self.scroll_x)
        else:
            self.horizontal_slider.disable()
            self.horizontal_slider.set_value(0)

        if show_h and show_v:
            self.corner_rect = pygame.FRect(
                self.viewport_rect.right,
                self.viewport_rect.bottom,
                self.slider_size,
                self.slider_size,
            )

    def _set_scroll_x(self, value):
        self.scroll_x = min(max(int(value), 0), self.max_scroll_x)
        if self.layout is not None:
            self.layout.apply(self.viewport_rect, offset_x = self.scroll_x, offset_y = self.scroll_y)

    def _set_scroll_y(self, value):
        self.scroll_y = min(max(int(value), 0), self.max_scroll_y)
        if self.layout is not None:
            self.layout.apply(self.viewport_rect, offset_x = self.scroll_x, offset_y = self.scroll_y)

    def _scroll_wheel(self, event):
        if self.max_scroll_y <= 0:
            return

        self._set_scroll_y(self.scroll_y - event.y * self.scroll_step)
        self.vertical_slider.set_value(self.scroll_y)
       
    
        
