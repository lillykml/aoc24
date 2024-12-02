# read in line by line and convert to integers
# check if either all elements differ by between -1 and -3 or 1 and 3
# if so, increment a safeLevels

safeLevels = 0
with open('input.txt', 'r') as f:
    for line in f:
        data = [int(x) for x in line.split()]
        if all(-3 <= data[i] - data[i+1] <= -1 for i in range(len(data) - 1)) or all(1 <= data[i] - data[i+1] <= 3 for i in range(len(data) - 1)):
            safeLevels += 1

print(safeLevels)