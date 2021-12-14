import pygame
import os


def move(x, y):
    image.(pose[0] + x, pose[1] + y)


if __name__ == '__main__':
    pygame.init()
    pygame.mouse.set_visible(False)
    screen = pygame.display.set_mode((300, 300))
    screen.fill((0, 0, 0))
    image = pygame.image.load(os.path.join('data', 'cursor.png'))
    image = image.convert()
    image.set_colorkey(image.get_at((0, 0)))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEMOTION:
                move(*event.rel)
            screen.blit(image, (10, 10))
        pygame.display.flip()

