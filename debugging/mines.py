#!/usr/bin/python3
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        if mines > width * height:
            raise ValueError("Number of mines cannot exceed total number of cells.")
        self.width = width
        self.height = height
        self.mines = set((m // width, m % width) for m in random.sample(range(width * height), mines))
        self.field = [[' ' for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]
        self.cells_to_reveal = width * height - mines  # Track non-mine cells to reveal

    def print_board(self, reveal=False):
        clear_screen()
        print('   ' + ' '.join(f"{i:2}" for i in range(self.width)))
        for y in range(self.height):
            print(f"{y:2} ", end="")
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if (y, x) in self.mines:
                        print('* ', end='')
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(f"{count} " if count > 0 else "  ", end='')
                else:
                    print('. ', end='')
            print()

    def count_mines_nearby(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height and (ny, nx) in self.mines:
                    count += 1
        return count

    def reveal(self, x, y):
        if (y, x) in self.mines:
            return False
        if self.revealed[y][x]:  # Prevent double recursion
            return True
        self.revealed[y][x] = True
        self.cells_to_reveal -= 1  # Decrease count of cells to reveal
        if self.count_mines_nearby(x, y) == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height:
                        self.reveal(nx, ny)
        return True

    def play(self):
        while True:
            self.print_board()
            try:
                print("Enter coordinates (x, y) to reveal a cell (e.g., '3 4'):")
                inputs = input("> ").strip().split()
                if len(inputs) != 2:
                    raise ValueError("Please enter exactly two numbers separated by a space.")
                x, y = map(int, inputs)
                if not (0 <= x < self.width and 0 <= y < self.height):
                    raise ValueError("Coordinates out of bounds.")
                if not self.reveal(x, y):
                    self.print_board(reveal=True)
                    print("Game Over! You hit a mine.")
                    break
                if self.cells_to_reveal == 0:  # Check for win condition
                    self.print_board(reveal=True)
                    print("Congratulations! You've won the game.")
                    break
            except ValueError as e:
                print(f"Error: {e}. Please try again.")

if __name__ == "__main__":
    game = Minesweeper()
    game.play()

