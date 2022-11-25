import numpy as np

from aocd import get_data, submit
from aocd.transforms import numbers

RED = '\033[91m'
ENDC = '\033[0m'


def inc_step(matrix):
    """increment all elements"""
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] += 1
    return matrix


def inc_bounded(matrix, i, j):
    """helper function so that inc_neighbors doesn't go out of bounds"""
    if i >= 0 and i < len(matrix): 
        if j >= 0 and j < len(matrix[i]):
            if matrix[i][j] != 0:  # don't increment if flashed
                matrix[i][j] += 1
    return matrix


def inc_neighbors(matrix, i, j):
    # top bottom
    matrix = inc_bounded(matrix, i+1, j)
    matrix = inc_bounded(matrix, i-1, j)

    # left right
    matrix = inc_bounded(matrix, i, j-1)
    matrix = inc_bounded(matrix, i, j+1)

    # diagonals
    matrix = inc_bounded(matrix, i-1, j-1)
    matrix = inc_bounded(matrix, i-1, j+1)
    matrix = inc_bounded(matrix, i+1, j-1)
    matrix = inc_bounded(matrix, i+1, j+1)
    return matrix


def flash_step(matrix):
    matrix = np.array(matrix)
    while len(matrix[matrix > 9]) > 0:
        # locate and flash all octopuses greater than 9
        rows, columns = np.where(matrix > 9)
        for i, j in zip(rows, columns):
            matrix[i][j] = 0
            matrix = inc_neighbors(matrix, i, j)
    return matrix


def flash_print(data):
    """helper function to highlight the 0s"""
    for row in data:
        row = ''.join([str(digit) for digit in row])
        print(row.replace('0', RED + '0' + ENDC))
    print()


DAY = 11
YEAR = 2021

raw_data = get_data(day=DAY, year=YEAR)

# part 1:
data = [[int(digit) for digit in row] for row in raw_data.splitlines()]
matrix = np.array(data)
total_flashes = 0
for x in range(100):
    data = inc_step(data)
    data = flash_step(data)
    total_flashes += len(data[data == 0])

print(total_flashes)
flash_print(data)


# part 2:
data = [[int(digit) for digit in row] for row in raw_data.splitlines()]
matrix = np.array(data)
step = 1
while True:
    data = inc_step(data)
    data = flash_step(data)
    if len(data[data != 0]) == 0:
        break
    step += 1

print(step)
flash_print(data)
