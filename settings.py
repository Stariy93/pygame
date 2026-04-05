# Разрешение экрана
import pygame


info = pygame.display.Info()
display_width = info.current_w
display_height = info.current_h
WIDTH = round(display_height * (9/19))
HEIGHT = display_height

# Настройки игры
FPS = 60
TITLE = "Pygame"

# Цвета (чтобы не писать каждый раз (255, 255, 255))
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)