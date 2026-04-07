import pygame
import widgets.button as button
import start_menu

class Main_menu():
    def __init__(self, manager):
        self.manager = manager
        self.btn_new_game = button.Button(100, 100, 30, "Back", action=lambda:self.go_back())

    def event(self, event):
        self.btn_new_game.event(event)

    def draw(self):
        self.btn_new_game.draw()

    def go_back(self):
        scene = start_menu.Start_menu(self.manager)
        self.manager.change_scene(scene)
