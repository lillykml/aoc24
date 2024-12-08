def read_input(file_path):

    a, b = [], []

    with open(file_path, 'r') as f:
        for line in f:
            (result, numbers) = line.split(':')
            numbers = [int(n) for n in numbers.split()]
            a.append(int(result))
            b.append(numbers)

    return a, b

def is_combination_possible(numbers, target):
    def backtrack(index, current_value):
        # Base case: If we've placed all operators, check if we hit the target
        if index == len(numbers):
            return current_value == target
        
        # Choose + or *
        next_value = numbers[index]
        return (
            # if either one is True overall is returned True
            backtrack(index + 1, current_value + next_value) or  # Add
            backtrack(index + 1, current_value * next_value) or    # Multiply
            backtrack(index + 1, int(str(current_value) + str(next_value)))   # Concatenate
        )
    
    # Start backtracking from the second number, with the first as the initial value
    return backtrack(1, numbers[0])

if __name__ == "__main__":
    file_path = 'input.txt'
    a,b = read_input(file_path)
    total = 0
    for result, numbers in zip(a, b):
        if (is_combination_possible(numbers, result)):
            total += result
    print(total)

