# read in input file (line by line)
# some regex to parse correct multiplications 
# multiply these numbers
import re

def read_input(file_path):
    
    input_string = ''

    with open(file_path, 'r') as f:
        for line in f:
            input_string += line

    return input_string


def find_matches(input):
    return re.findall(r"mul\(\b([0-9]{1,3})\b,\b([0-9]{1,3})\b\)", input)


if __name__ == "__main__":
    file_path = 'input.txt'
    input = read_input(file_path)
    matches = find_matches(input)
    result = sum([int(match[0]) * int(match[1]) for match in matches])
    print(result)