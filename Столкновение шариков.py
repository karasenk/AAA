from random import choice
import pygame

horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()
balls = pygame.sprite.Group()


class Ball(pygame.sprite.Sprite):
    def __init__(self, radius, x, y):
        super().__init__(balls)
        self.add(balls)
        self.radius = radius
        self.image = pygame.Surface((2 * radius, 2 * radius),
                                    pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color("red"),
                           (radius, radius), radius)
        self.rect = pygame.Rect(x, y, 2 * radius, 2 * radius)
        self.vx = choice([x for x in range(110, 120)] + [x for x in range(-100, -120)])
        self.vy = choice([x for x in range(110, 120)] + [x for x in range(-100, -120)])

    def update(self):
        coef = clock.tick(fps) / fps
        self.rect = self.rect.move(coef * self.vx, coef * self.vy)
        if pygame.sprite.spritecollideany(self, horizontal_borders):
            self.vy = -self.vy
        if pygame.sprite.spritecollideany(self, vertical_borders):
            self.vx = -self.vx


class Border(pygame.sprite.Sprite):
    # строго вертикальный или строго горизонтальный отрезок
    def __init__(self, x1, y1, x2, y2):
        if x1 == x2:  # вертикальная стенка
            super().__init__(vertical_borders)
            self.add(vertical_borders)
            self.image = pygame.Surface([1, y2 - y1])
            self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
        else:  # горизонтальная стенка
            super().__init__(horizontal_borders)
            self.add(horizontal_borders)
            self.image = pygame.Surface([x2 - x1, 1])
            self.rect = pygame.Rect(x1, y1, x2 - x1, 1)


pygame.init()
width = 500
height = 500
Border(5, 5, width - 5, 5)
Border(5, height - 5, width - 5, height - 5)
Border(5, 5, 5, height - 5)
Border(width - 5, 5, width - 5, height - 5)
for i in range(10):
    Ball(20, 100, 100)
screen = pygame.display.set_mode((500, 500))
screen.fill((0, 0, 0))
pygame.display.set_caption('Balls')
clock = pygame.time.Clock()
run = True
fps = 70
clock.tick(fps)
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill((255, 255, 255))
    balls.draw(screen)
    balls.update()
    vertical_borders.draw(screen)
    horizontal_borders.draw(screen)
    pygame.display.flip()
pygame.quit()
