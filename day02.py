from aocd import get_data
from aocd.transforms import lines
from aocd import submit

DAY = 2
YEAR = 2021

# get data
raw_data = get_data(day=DAY, year=YEAR)
data = lines(raw_data)


# part a
def parse(command, position):
    horizontal_pos = position[0]
    depth = position[1]
    X = int(command.split(' ')[-1])

    if command.startswith('forward'):
        return (horizontal_pos + X, depth)
    elif command.startswith('up'):
        return (horizontal_pos, depth - X)
    elif command.startswith('down'):
        return (horizontal_pos, depth + X)
    else:
        print(f'bad command data: {command}')


position = (0, 0)
for command in data:
    position = parse(command, position)

solution_a = position[0] * position[1]
submit(solution_a, part="a", day=DAY, year=YEAR)


# part b
def parse(command, position):
    horizontal_pos = position[0]
    depth = position[1]
    aim = position[2]
    X = int(command.split(' ')[-1])

    if command.startswith('forward'):
        return (horizontal_pos + X, depth + aim * X, aim)
    elif command.startswith('up'):
        return (horizontal_pos, depth, aim - X)
    elif command.startswith('down'):
        return (horizontal_pos, depth, aim + X)
    else:
        print(f'bad command data: {command}')


position = (0, 0, 0)
for command in data:
    position = parse(command, position)

solution_b = position[0] * position[1]
submit(solution_b, part="b", day=DAY, year=YEAR)
