import pygame

import widgets.button as button
import main_menu
import settings
import widgets.panel as panel
import Boxes.HBox as HBox

class Start_menu():
    def __init__(self, manager):
        self.manager = manager
        self.panel = panel.Panel(100, 200, settings.WIDTH - 200, settings.HEIGHT - 400)
        self.p = panel.Panel(10, 20, 200, 200, color=(100,100,100))
        self.btn_new_game = button.Button(text = "Start", action=lambda: self.go_to_mein_menu())
        self.btn_exit = button.Button(text = "Exit", action=lambda: self.exit())
        self.layout = HBox.HBox(pos="bottom", rect=self.panel.rect, gap = 10, padding=10)
        self.layout.add(self.btn_new_game)
        self.layout.add(self.btn_exit)
        self.layout.add(self.p)
        self.layout.apply()

    def event(self, event):
        self.btn_new_game.event(event)
        self.btn_exit.event(event)

    def draw(self):
        self.panel.draw()
        self.btn_new_game.draw()
        self.btn_exit.draw()
        self.p.draw()

    def go_to_mein_menu(self):
        next_scene = main_menu.Main_menu(self.manager)
        self.manager.change_scene(next_scene)

    def exit(self):
        self.manager.exit_game()
        
        

