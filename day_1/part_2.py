from collections import Counter

def read_input(file_path):

    a, b = [], Counter()

    with open(file_path, 'r') as f:
        for line in f:
            x, y = line.split()
            a.append(x)
            b[y] += 1

    return a, b

def calculate_similarity_score(a,b):
    return sum(int(x) * b[x] for x in a if x in b)


if __name__ == "__main__":
    file_path = 'input.txt'
    a,b = read_input(file_path)
    score = calculate_similarity_score(a, b)
    print(score)