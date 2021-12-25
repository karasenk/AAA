import pygame
from random import sample


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[-1] * width for _ in range(height)]
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


class Minesweeper(Board):
    def __init__(self, w, h, count):
        super().__init__(w, h)
        mines = sample(range(0, w * h), count)
        for m in mines:
            self.board[m // h][m % h] = 10

    def render(self, screen):
        super().render(screen)
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == 10:
                    rect = (self.left + j * self.cell_size, self.top + i *
                            self.cell_size), (self.cell_size, self.cell_size)
                    pygame.draw.rect(screen, (255, 0, 0), rect)

    def open_cell(self):
        pass

