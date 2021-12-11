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

    def get_click(self, mouse_pos, event):
        cell = self.get_cell(mouse_pos)
        if cell:
            if event.button == 1:
                self.add(cell)
            elif event.button == 3:
                self.living()

    def add(self, cell):
        self.board[cell[0]][cell[1]] = 1
        rect = self.left + cell[1] * self.cell_size, self.top + cell[0] * self.cell_size,\
               self.cell_size, self.cell_size
        pygame.draw.rect(screen, (50, 230, 5), rect)

    def living(self);
     pass
    def next_move(self):
        pass

if '__main__' == __name__:
    pygame.init()
    size = 400, 300
    screen = pygame.display.set_mode(size)
    life = Life(12, 9)
    running = True
    screen.fill((0, 0, 0))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                life.get_click(event.pos, event)
        life.render(screen)
        pygame.display.flip()
