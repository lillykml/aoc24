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

if __name__ == "__main__":
    file_path = 'input.txt'
    letters = read_input(file_path)
    total = 0

    # horizontal
    for line in letters:
      total += get_number_of_xmas(''.join(line))
      total += get_number_of_xmas(reverse(''.join(line)))
    
    # vertical
    for col in range(len(letters[0])):
        vertical_line = ''.join(letters[row][col] for row in range(len(letters)))
        total += get_number_of_xmas(vertical_line)
        total += get_number_of_xmas(reverse(vertical_line))

    # For diagonals (top-left to bottom-right)
    for start_col in range(len(letters[0])):
        # Start from each position in first row
        diagonal = ''.join(letters[i][start_col + i] 
                        for i in range(min(len(letters), len(letters[0]) - start_col)))
        total += get_number_of_xmas(diagonal)
        total += get_number_of_xmas(reverse(diagonal))

    # Start from each position in first column (except first row which we already did)
    for start_row in range(1, len(letters)):
        diagonal = ''.join(letters[start_row + i][i] 
                        for i in range(min(len(letters) - start_row, len(letters[0]))))
        total += get_number_of_xmas(diagonal)
        total += get_number_of_xmas(reverse(diagonal))

    # For diagonals (top-right to bottom-left)
    for start_col in range(len(letters[0])):
        # Start from each position in first row
        diagonal = ''.join(letters[i][start_col - i] 
                        for i in range(min(len(letters), start_col + 1)))
        total += get_number_of_xmas(diagonal)
        total += get_number_of_xmas(reverse(diagonal))

    # Start from each position in first column (except first row which we already did)
    for start_row in range(1, len(letters)):
        diagonal = ''.join(letters[start_row + i][len(letters[0])-1 - i] 
                        for i in range(min(len(letters) - start_row, len(letters[0]))))
        total += get_number_of_xmas(diagonal)
        total += get_number_of_xmas(reverse(diagonal))
        
    print(total)