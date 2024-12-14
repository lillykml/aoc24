# read in file into a 2x2 array?
# horizontal, vertical, diagonal and everything backwards
# brute force go through all this and find xms
# or construct 4 strings and then do regex and findall 

import re

def read_input(file_path):
    with open(file_path, 'r') as f:
        return [list(line.strip()) for line in f]

def get_number_of_xmas(input_text):
    return len(re.findall(r"XMAS", input_text))

def reverse(input_text):
    return input_text[::-1]


def count_xmas(grid, word="XMAS"):
    rows, cols = len(grid), len(grid[0])
    word_len = len(word)
    directions = [
        (0, 1),    # Right
        (1, 0),    # Down
        (1, 1),    # Down-right
        (1, -1),   # Down-left
        (0, -1),   # Left
        (-1, 0),   # Up
        (-1, -1),  # Up-left
        (-1, 1)    # Up-right
    ]
    count = 0

    def is_valid(x, y, dx, dy):
        """Check if word fits starting at (x, y) in direction (dx, dy)."""
        for i in range(word_len):
            nx, ny = x + i * dx, y + i * dy
            if nx < 0 or ny < 0 or nx >= rows or ny >= cols or grid[nx][ny] != word[i]:
                return False
        return True

    for x in range(rows):
        for y in range(cols):
            for dx, dy in directions:
                if is_valid(x, y, dx, dy):
                    count += 1

    return count

if __name__ == "__main__":
    file_path = 'input.txt'
    letters = read_input(file_path)
    print(count_xmas(letters))

