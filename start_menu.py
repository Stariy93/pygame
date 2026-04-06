import pygame

import button
import main_menu
import settings
import panel
import VBox

class Start_menu():
    def __init__(self, manager):
        self.manager = manager
        self.panel = panel.Panel(0, 0, settings.WIDTH, settings.HEIGHT)
        self.btn_new_game = button.Button(text = "Start", action=lambda: self.go_to_mein_menu())
        self.btn_exit = button.Button(text = "Exit", action=lambda: self.exit())
        self.layout = VBox.VBox(pos="center", rect=self.panel.rect, gap = 10, padding=settings.HEIGHT//3)
        self.layout.add(self.btn_new_game)
        self.layout.add(self.btn_exit)
        self.layout.apply()

    def event(self, event):
        self.btn_new_game.event(event)
        self.btn_exit.event(event)

    def draw(self):
        self.panel.draw()
        self.btn_new_game.draw()
        self.btn_exit.draw()

    def go_to_mein_menu(self):
        next_scene = main_menu.Main_menu(self.manager)
        self.manager.change_scene(next_scene)

    def exit(self):
        self.manager.exit_game()
        
        

