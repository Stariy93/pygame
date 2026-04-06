import pygame

# 1. Инициализация Pygame
pygame.init()
import scene_manager
import start_menu


game = scene_manager.Scene_manager(None)

first_scene = start_menu.Start_menu(game)

game.change_scene(first_scene)

game.game()
