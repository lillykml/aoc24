import re

def read_input(file_path):
    
    input_string = ''

    with open(file_path, 'r') as f:
        for line in f:
            input_string += line

    return input_string


def find_matches(input):
    return re.findall(r"mul\(\b[0-9]{1,3}\b,\b[0-9]{1,3}\b\)|do\(\)|don't\(\)", input)


if __name__ == "__main__":
    file_path = 'input.txt'
    input = read_input(file_path)
    matches = find_matches(input)
    do = True
    result = 0
    print(matches)
    for match in matches:
        if match.startswith('mul') and do:
            numbers = re.findall(r'\d+', match)
            result += int(numbers[0]) * int(numbers[1])
        elif match == 'do()': 
            do = True
        else:
            do = False
    print(result)