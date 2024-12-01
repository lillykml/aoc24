# read in input file
# split into 2 arrays on the empty string
# sort the arrays
# subtract the elements, take the absolute value, and sum the result

def read_input(file_path):

    a, b = [], []

    with open(file_path, 'r') as f:
        for line in f:
            data = line.split()
            a.append(int(data[0]))
            b.append(int(data[1]))

    return a, b

def calculate_difference(a, b):
    a_sorted, b_sorted = sorted(a), sorted(b)
    return sum(abs(x - y) for x, y in zip(a_sorted, b_sorted))

if __name__ == "__main__":
    file_path = 'input.txt'
    a,b = read_input(file_path)
    diff = calculate_difference(a, b)
    print(diff)