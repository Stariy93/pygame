import pygame


class Cell(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_frect(topleft = (x, y))

    def update(self, dt):
        self.rect.x += 100 * dt

