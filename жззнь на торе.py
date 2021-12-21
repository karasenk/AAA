import pygame


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for i in range(self.height):
            for j in range(self.width):
                rect = (self.left + j * self.cell_size, self.top + i *
                        self.cell_size), (self.cell_size, self.cell_size)
                pygame.draw.rect(screen, (255, 255, 255), rect, 1)

    def get_cell(self, mouse_pos):
        result = None
        for i in range(self.height):
            for j in range(self.width):
                if self.left + j * self.cell_size <= mouse_pos[0] and \
                        self.left + (j + 1) * self.cell_size >= mouse_pos[0] and \
                        self.top + i * self.cell_size <= mouse_pos[1] and \
                        self.top + (i + 1) * self.cell_size >= mouse_pos[1]:
                    result = i, j
                    break
        print(result)
        return result

    def on_click(self, cell):
        pass

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            self.on_click(cell)


class Life(Board):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.life = False

    def get_click(self, event):
        cell = self.get_cell(event.pos)
        if cell and not self.life:
            if event.button == 1:
                self.add(cell)

    def add(self, cell):
        self.board[cell[0]][cell[1]] = 1
        rect = self.left + cell[1] * self.cell_size, self.top + cell[0] * self.cell_size,\
               self.cell_size, self.cell_size
        pygame.draw.rect(screen, (50, 230, 5), rect)

    def delete(self, cell):
        self.board[cell[0]][cell[1]] = 0
        rect = self.left + cell[1] * self.cell_size, self.top + cell[0] * self.cell_size,\
               self.cell_size, self.cell_size
        pygame.draw.rect(screen, (0, 0, 0), rect)

    def death(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] != 0:
                    return False
        print('все умерли')
        return True

    def check_neighbors(self, i, j):
        alive = 0
        for x in range(i - 1, i + 2):
            x1 = x
            if x >= len(self.board):
                x1 = x % (len(self.board) - 1)
            elif x < 0:
                x1 = len(self.board) - 1 - abs(x)
            for y in range(j - 1, j + 2):
                y1 = y
                if y >= len(self.board[0]):
                    y1 = y % (len(self.board[0]) - 1)
                elif y < 0:
                    y1 = len(self.board[0]) - 1 - abs(y)
                if self.board[x1][y1] == 1 and not (x == i and y == j):
                    alive += 1
        return alive

    def next_move(self):
        if not self.death():
            for i in range(len(self.board)):
                for j in range(len(self.board[i])):
                    alive = self.check_neighbors(i, j)
                    if self.board[i][j] == 0:
                        if alive == 3:
                            self.add((i, j))
                    else:
                        if alive != 2 and alive != 3:
                            self.delete((i, j))
                    if j + 1 == len(self.board[i]) and i + 1 != len(self.board):
                        alive = self.check_neighbors(i, j + 1)
                        if alive == 3:
                            self.add((i, 0))
                if i + 1 == len(self.board):
                    alive = self.check_neighbors(i + 1, len(self.board[0]))
                    if alive == 3:
                        self.add((0, 0))
        else:
            self.life = False


if '__main__' == __name__:
    pygame.init()
    clock = pygame.time.Clock()
    fps = 5
    size = 400, 300
    screen = pygame.display.set_mode(size)
    life = Life(12, 9)
    running = True
    screen.fill((0, 0, 0))
    while running:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 4 and life.life:
                    fps += 10
                    print('faster')
                elif event.button == 5 and life.life:
                    if fps - 10 > 0:
                        fps -= 10
                    print('slower')
                elif event.button == 3:
                    life.life = True
                else:
                    life.get_click(event)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    if life.life:
                        life.life = False
                    else:
                        life.life = True

        if life.life:
            life.next_move()
        life.render(screen)
        pygame.display.flip()
    pygame.quit()
