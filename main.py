import pygame

# 1. Инициализация Pygame
pygame.init()
import scene_manager as scene_manager
import scenes.start_menu as start_menu


game = scene_manager.SceneManager(None)

first_scene = start_menu.StartMenu(game)

game.change_scene(first_scene)

game.game()
