import pygame


def draw(screen, n):
    screen.fill((0, 0, 0))
    step = 300 // n
    for i in range(1, n + 1):
        r0 = ((0, 150 - 150 // i), (300, 300 // i))  # горизонтальные
        r1 = ((150 - 150 // i, 0), (300 // i, 300))  # вертикальные
        pygame.draw.ellipse(screen, pygame.Color(255, 255, 255), r0, width=1)
        pygame.draw.ellipse(screen, pygame.Color(255, 255, 255), r1, width=1)


n = input()
if n.isdigit():
    pygame.init()
    n = int(n)
    screen = pygame.display.set_mode((300, 300))
    pygame.display.set_caption('сфера')
    draw(screen, n)
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        draw(screen, n)
    pygame.quit()
else:
    print('Неправильный формат ввода')
