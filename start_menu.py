import button
import main_menu
import settings

class Start_menu():
    def __init__(self, manager):
        self.manager = manager
        self.btn_new_game = button.Button(settings.WIDTH//2, settings.HEIGHT//2, 30, "Start", action=lambda: self.go_to_mein_menu())

    def event(self, event):
        self.btn_new_game.event(event)

    def draw(self):
        self.btn_new_game.draw()

    def go_to_mein_menu(self):
        next_scene = main_menu.Main_menu(self.manager)
        self.manager.change_scene(next_scene)
        
        

