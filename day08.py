from aocd import get_data, submit
from aocd.transforms import lines

DAY = 8
YEAR = 2021

# get data
raw_data = get_data(day=DAY, year=YEAR)
data = lines(raw_data)

# part a
solution_a = 0
for line in data:
    outputs = line.split('|')[1].split()
    for num in map(len, outputs):
        if num in [2, 4, 3, 7]:
            solution_a += 1
submit(solution_a, part='a', day=DAY, year=YEAR)

# part b
solution_b = 0
for line in data:
    solution = {}
    inputs = line.split('|')[0].split()
    outputs = line.split('|')[1].split()

    len5 = []
    len6 = []
    for token in inputs:
        if len(token) == 2:
            solution[1] = set(token)
        elif len(token) == 4:
            solution[4] = set(token)
        elif len(token) == 3:
            solution[7] = set(token)
        elif len(token) == 7:
            solution[8] = set(token)
        elif len(token) == 5:
            len5.append(set(token))
        elif len(token) == 6:
            len6.append(set(token))

    for token in len5:
        if solution[1].issubset(token):
            solution[3] = token
            break

    for token in len6:
        if not solution[1].issubset(token):
            solution[6] = token
            break

    for token in len5:
        diff = len(token.symmetric_difference(solution[6]))
        if diff == 1:
            solution[5] = token
        elif diff == 3 and token != solution[3]:
            solution[2] = token

    for token in len6:
        diff = len(token.symmetric_difference(solution[3]))
        if diff == 1:
            solution[9] = token
        elif diff == 3 and token != solution[6]:
            solution[0] = token

    num_str = ''
    for output in outputs:
        for k, token in solution.items():
            if set(output) == token:
                num_str += str(k)
    solution_b += int(num_str)

print(solution_b)
submit(solution_b, part='b', day=DAY, year=YEAR)
