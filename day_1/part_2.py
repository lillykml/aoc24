# read in input file
# split on the empty string
# for the second array don't store in a list but in a dictionary
# add key if not present otherwise add 1 

def read_input(file_path):

    a, b = [], {}

    with open(file_path, 'r') as f:
        for line in f:
            data = line.split()
            a.append(data[0])
        
            if (data[1]) in b:
                b[(data[1])] += 1
            else:
                b[(data[1])] = 1

    return a, b

def calculate_similarity_score(a,b):
    score = 0
    for item in a:
        if item in b:
            score += int(item) * b[item]
    return score


if __name__ == "__main__":
    file_path = 'input.txt'
    a,b = read_input(file_path)
    score = calculate_similarity_score(a, b)
    print(score)