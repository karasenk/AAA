import pygame

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('шарики')
    v = 100
    size = 500, 500
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    running = True
    draw = False
    screen.fill((0, 0, 0))
    coords = []
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                screen.fill((0, 0, 0))
                draw = True
                coords.append([event.pos, 1])
                pygame.draw.circle(screen, (255, 200, 250), event.pos, 10)
        if draw:
            for c in coords:
                if c[0] + 1 >= size[0]:
                    coef = -1
                pygame.draw.circle(screen, (255, 200, 250), pose, 10)

        pygame.display.flip()
    pygame.quit()

#  сделой коеффициент (1 и -1) для направления
