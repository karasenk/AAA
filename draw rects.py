import pygame


def draw_rect(pos0, pos1):
    screen.fill((0, 0, 0))
    w, h = pos0[0] - pos1[0], pos0[1] - pos1[1]
    pygame.draw.rect(screen, (255, 255, 255), (pos1, (w, h)), width=1)


def main():
    running = True
    draw = False
    pos = 0, 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                draw = True
                pos = event.pos
            elif event.type == pygame.MOUSEBUTTONUP:
                draw = False
            elif event.type == pygame.MOUSEMOTION:
                if draw:
                    draw_rect(event.pos, pos)
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    main()
