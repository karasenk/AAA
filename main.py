import pygame


def draw(screen, w, h, side):
    screen.fill((0, 0, 0))
    lefttop = side // 2 - (w + w // 2) // 2
    rect = (lefttop, lefttop, w, w)
    color = pygame.Color(255, 0, 0)
    clr = color.hsva
    color.hsva = (h, clr[1], int(clr[2] * 0.75))
    pygame.draw.rect(screen, color, rect)
    color.hsva = (h, clr[1], clr[2])
    pygame.draw.polygon(screen, color, [(lefttop, lefttop),
                                        (lefttop + w // 2, lefttop - w // 2),
                                        (lefttop + int(w * 1.5), lefttop - w // 2),
                                        (lefttop + w, lefttop)])
    color.hsva = (h, clr[1], clr[2] // 2)
    pygame.draw.polygon(screen, color, [(lefttop + w, lefttop),
                                        (lefttop + int(w * 1.5), lefttop - w // 2),
                                        (lefttop + int(w * 1.5), lefttop + w // 2),
                                        (lefttop + w, lefttop + w)])



numbers = input()
if len(numbers.split()) == 2 and numbers.split()[0].isdigit() and \
        numbers.split()[1].isdigit() and numbers.count(' ') == 1:
    w, h = list(map(int, numbers.split()))
    if w % 4 == 0 and w <= 100 and h <= 360 and w > 0 and h >= 0:
        pygame.init()
        side = 300
        screen = pygame.display.set_mode((side, side))
        pygame.display.set_caption('куб')
        draw(screen, w, h, side)
        pygame.display.flip()
        while pygame.event.wait().type != pygame.QUIT:
            draw(screen, w, h, side)
        pygame.quit()
    else:
        print('Неправильный формат ввода')
else:
    print('Неправильный формат ввода')
