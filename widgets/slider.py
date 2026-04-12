import pygame
from widgets.widget import Widget


class Slider(Widget):
    def __init__(self, x = 0, y = 0, width = 260, min_value = 0, max_value = 100,
                 value = 0, step = 1, action = None, file_path = "sprites/lever.png",
                 orientation = "horizontal"):
        super().__init__()
        if max_value <= min_value:
            raise ValueError("Slider max_value must be greater than min_value")
        if step <= 0:
            raise ValueError("Slider step must be greater than 0")
        if orientation not in ("horizontal", "vertical"):
            raise ValueError("Slider orientation must be 'horizontal' or 'vertical'")

        base_image = pygame.image.load(file_path).convert_alpha()
        self.orientation = orientation
        self.image = base_image if self.orientation == "horizontal" else pygame.transform.rotate(base_image, 90)
        self.min_value = min_value
        self.max_value = max_value
        self.step = step
        self.action = action
        self.dragging = False
        self.length = max(width, self.image.get_width() + 20)

        slider_width, slider_height = self._get_slider_size(self.length)
        self.rect = pygame.FRect(x, y, slider_width, slider_height)
        self.track_height = max(6, self.image.get_height() // 5)
        self.track_rect = pygame.FRect(0, 0, 0, 0)
        self.lever_rect = self.image.get_rect()
        self.value = self._normalize_value(value)
        self._update_layout()
        self._sync_lever_to_value()

    def _draw(self):
        pygame.draw.rect(self.screen, "grey30", self.track_rect, border_radius = self.track_height // 2)

        filled_rect = None
        if self.orientation == "horizontal":
            filled_width = self.lever_rect.centerx - self.track_rect.left
            if filled_width > 0:
                filled_rect = pygame.FRect(self.track_rect.left, self.track_rect.top, filled_width, self.track_rect.height)
        else:
            filled_height = self.track_rect.bottom - self.lever_rect.centery
            if filled_height > 0:
                filled_rect = pygame.FRect(self.track_rect.left, self.lever_rect.centery, self.track_rect.width, filled_height)

        if filled_rect is not None:
            pygame.draw.rect(self.screen, "grey60", filled_rect, border_radius = self.track_height // 2)

        self.screen.blit(self.image, self.lever_rect)

    def _event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.lever_rect.collidepoint(event.pos) or self.rect.collidepoint(event.pos):
                self.dragging = True
                self._set_value_from_mouse(event.pos)

        elif event.type == pygame.MOUSEMOTION and self.dragging:
            self._set_value_from_mouse(event.pos)

        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.dragging:
                self._set_value_from_mouse(event.pos)
            self.dragging = False

    def set_position(self, pos = "center", x = 0, y = 0):
        super().set_position(pos, x, y)
        self._update_layout()
        self._sync_lever_to_value()

    def set_rect(self, rect):
        self.rect = pygame.FRect(rect)
        self.length = self.rect.width if self.orientation == "horizontal" else self.rect.height
        self._update_layout()
        self._sync_lever_to_value()

    def set_value(self, value, trigger_action = False):
        normalized_value = self._normalize_value(value)
        changed = normalized_value != self.value
        self.value = normalized_value
        self._sync_lever_to_value()
        if changed and trigger_action:
            self._trigger_action()

    def get_value(self):
        return self.value

    def _get_slider_size(self, length):
        if self.orientation == "horizontal":
            return max(length, self.image.get_width() + 20), max(self.image.get_height(), 12)
        return max(self.image.get_width(), 12), max(length, self.image.get_height() + 20)

    def _update_layout(self):
        if self.orientation == "horizontal":
            lever_half_width = self.lever_rect.width / 2
            track_width = max(1, self.rect.width - self.lever_rect.width)
            self.track_rect = pygame.FRect(
                self.rect.left + lever_half_width,
                self.rect.centery - self.track_height / 2,
                track_width,
                self.track_height,
            )
        else:
            lever_half_height = self.lever_rect.height / 2
            track_height = max(1, self.rect.height - self.lever_rect.height)
            self.track_rect = pygame.FRect(
                self.rect.centerx - self.track_height / 2,
                self.rect.top + lever_half_height,
                self.track_height,
                track_height,
            )

    def _set_value_from_mouse(self, mouse_pos):
        ratio = 0
        if self.orientation == "horizontal":
            clamped_pos = min(max(mouse_pos[0], self.track_rect.left), self.track_rect.right)
            if self.track_rect.width > 0:
                ratio = (clamped_pos - self.track_rect.left) / self.track_rect.width
        else:
            clamped_pos = min(max(mouse_pos[1], self.track_rect.top), self.track_rect.bottom)
            if self.track_rect.height > 0:
                ratio = (clamped_pos - self.track_rect.top) / self.track_rect.height
            ratio = 1 - ratio

        raw_value = self.min_value + ratio * (self.max_value - self.min_value)
        new_value = self._normalize_value(raw_value)
        if new_value != self.value:
            self.value = new_value
            self._trigger_action()
        self._sync_lever_to_value()

    def _sync_lever_to_value(self):
        ratio = (self.value - self.min_value) / (self.max_value - self.min_value)
        if self.orientation == "horizontal":
            self.lever_rect.center = (
                round(self.track_rect.left + ratio * self.track_rect.width),
                round(self.rect.centery),
            )
        else:
            self.lever_rect.center = (
                round(self.rect.centerx),
                round(self.track_rect.bottom - ratio * self.track_rect.height),
            )

    def _normalize_value(self, value):
        clamped_value = min(max(value, self.min_value), self.max_value)
        steps = round((clamped_value - self.min_value) / self.step)
        normalized_value = self.min_value + steps * self.step
        normalized_value = min(max(normalized_value, self.min_value), self.max_value)

        if isinstance(self.min_value, int) and isinstance(self.max_value, int) and isinstance(self.step, int):
            return int(round(normalized_value))
        return normalized_value

    def _trigger_action(self):
        if self.action is None:
            return

        try:
            self.action(self.value)
        except TypeError:
            self.action()