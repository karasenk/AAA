<<<<<<< HEAD
import pygame

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('к щелчку')
    size = 501, 501
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    running = True
    v = 50
    pose = (size[0] // 2, size[1] // 2)
    goal = False
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (0, 255, 0), pose, 20)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                goal = event.pos
            if goal:
                if pose == goal:
                    goal = False
                else:
                    diff_x = goal[0] - pose[0]
                    diff_y = goal[1] - pose[1]
                    if diff_x != 0:
                        x = diff_x // abs(diff_x) * v * clock.tick() / 1000
                    if diff_y != 0:
                        y = diff_y // abs(diff_y) * v * clock.tick() / 1000
                    if abs(diff_x) > abs(diff_y):
                        y = 0
                    elif abs(diff_x) < abs(diff_y):
                        x = 0
                    pose = pose[0] + x, pose[1] + y
                    screen.fill((0, 0, 0))
                    pygame.draw.circle(screen, (0, 255, 0), pose, 20)

        pygame.display.flip()
    pygame.quit()
=======
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
>>>>>>> origin/master
