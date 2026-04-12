import pygame
import widgets.button as button
import scenes.start_menu as start_menu
import widgets.button_i as button_i
import boxes.v_box as v_box
from widgets.panel import Panel
from widgets.spaser import Spacer
from widgets.text import Text

class MainMenu():
    def __init__(self, manager):
        self.manager = manager
        self.btn_back = button_i.ButtonI(text="back", action=lambda:self.go_back())
        self.panel = Panel(420, 110, 760, 460, color = (210, 220, 235), padding = 18)
        self.box = v_box.VBox("center", self.panel.rect, gap = 20, padding = 24)
        self.panel.set_layout(self.box)
        self.title = Text(54, "Scrollable panel content clips outside the viewport")
        self.box.add(self.title)
        self.box.add(Spacer(height = 10))
        self.box.add(self.btn_back)

        for index in range(1, 9):
            self.box.add(button_i.ButtonI(text = f"demo {index}", action = self._noop))

        self.box.add(Spacer(height = 140))
        self.panel._refresh_layout()

    def event(self, event):
        self.panel.event(event)

    def draw(self):
        self.panel.draw()

    def _noop(self):
        pass

    def go_back(self):
        scene = start_menu.StartMenu(self.manager)
        self.manager.change_scene(scene)
