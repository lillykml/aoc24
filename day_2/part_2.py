def is_safe(data):
    diffs = [data[i + 1] - data[i] for i in range(len(data) - 1)]
    return all(-3 <= diff <= -1 for diff in diffs) or all(1 <= diff <= 3 for diff in diffs)

safeLevels = 0
with open('input.txt', 'r') as f:
    for line in f:
        data = [int(x) for x in line.split()]

        if is_safe(data):
            safeLevels += 1
        else: 
            for i in range(len(data)):
                modified_data = data[:i] + data[i+1:]
                if is_safe(modified_data):
                    safeLevels += 1
                    break
                
print(safeLevels)