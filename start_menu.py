import pygame

import button
import main_menu
import settings

class Start_menu():
    def __init__(self, manager):
        self.manager = manager
        self.btn_new_game = button.Button(settings.WIDTH//2, settings.HEIGHT//2, 30, "Start", action=lambda: self.go_to_mein_menu())
        self.btn_exit = button.Button(settings.WIDTH//2, settings.HEIGHT//2 + self.btn_new_game.rect.height + 30, 30, "Exit", action=lambda: self.exit())

    def event(self, event):
        self.btn_new_game.event(event)
        self.btn_exit.event(event)

    def draw(self):
        self.btn_new_game.draw()
        self.btn_exit.draw()

    def go_to_mein_menu(self):
        next_scene = main_menu.Main_menu(self.manager)
        self.manager.change_scene(next_scene)

    def exit(self):
        self.manager.exit_game()
        
        

