import pygame
import sys
import settings as set

class Scene_manager():
    def __init__(self, scene):
        self.scene = scene
        self.clock = pygame.time.Clock()
        self.width, self.height = set.WIDTH, set.HEIGHT
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(set.TITLE)

    def change_scene(self, new_scene):
        self.scene = new_scene

    def game(self):
        running = True
        while running:
            dt = self.clock.tick(set.FPS) / 1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False  
                self.scene.event(event)
            self.screen.fill((255, 255, 255))
            self.scene.draw()
            pygame.display.flip()
            
        # 5. Корректное завершение работы
        pygame.quit()
        sys.exit()