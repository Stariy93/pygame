import pygame

import scenes.main_menu as main_menu
import settings
import boxes.v_box as v_box
import widgets.button_i as ButtonM
import widgets.image as ImageM
from widgets.spaser import Spacer
from widgets.slider import Slider

class StartMenu():
    def __init__(self, manager):
        self.manager = manager
        self.background = ImageM.Image(file_path="sprites/background_menu.png")
        self.btn_start = ButtonM.ButtonI(text="start", action = lambda: self.go_to_mein_menu())
        self.btn_exit = ButtonM.ButtonI(text="exit", action=lambda:self.exit())
        self.volume_slider = Slider(
    width=240,
    min_value=0,
    max_value=100,
    value=0,
    step=1,
    action=lambda value: print(value)
)
        self.vbox = v_box.VBox("center", self.background.rect)
        self.vbox.add(self.btn_start)
        self.vbox.add(Spacer(height=100))
        self.vbox.add(self.btn_exit)
        self.vbox.add(self.volume_slider)
        self.vbox.apply()
        

    def event(self, event):
        self.vbox.event(event)

    def draw(self):
        self.background.draw()
        self.vbox.draw()

    def go_to_mein_menu(self):
        next_scene = main_menu.MainMenu(self.manager)
        self.manager.change_scene(next_scene)

    def exit(self):
        self.manager.exit_game()
        
        

