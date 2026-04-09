import pygame

import widgets.button as button
import main_menu
import settings
import widgets.panel as panel
import Boxes.HBox as HBox
import widgets.Text as Text
import widgets.Button_i as ButtonM

class Start_menu():
    def __init__(self, manager):
        self.manager = manager
        self.b = ButtonM.Button_i(action = lambda: self.go_to_mein_menu())
        

    def event(self, event):
        self.b.event(event)

    def draw(self):
        self.b.draw()

    def go_to_mein_menu(self):
        next_scene = main_menu.Main_menu(self.manager)
        self.manager.change_scene(next_scene)

    def exit(self):
        self.manager.exit_game()
        
        

