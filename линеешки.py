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


class Lines(Board):
    def __init__(self, w, h):
        super().__init__(w, h)
        self.find = False

    def on_click(self, cell):
        x, y = cell
        if self.board[x][y] == 0:
            self.board[x][y] = 1
            if self.find:
                self.find_path(cell)
        elif self.board[x][y] == 1:
            self.board[x][y] = 2
            self.find = cell

    def find_path(self, cell):
        if cell != self.find:
            pass

