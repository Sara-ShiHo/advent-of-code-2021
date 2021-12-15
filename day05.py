from aocd import get_data, submit
from aocd.transforms import lines
import numpy as np
import re

DAY = 5
YEAR = 2021


# get data
raw_data = get_data(day=DAY, year=YEAR)
data = [re.findall(r'(\d+),(\d+) -> (\d+),(\d+)', line)[0] for line in lines(raw_data)]
data = [[*map(int, row)] for row in data]


def ranges(a, b):
    """
    increment or decrement a in order to reach b
    """
    if a > b:
        return range(a, b-1, -1)
    else:
        return range(a, b+1)


# part a
canvas = np.zeros((np.max(data) + 1, np.max(data) + 1))
for x1, y1, x2, y2 in data:
    if x1 == x2 and y1 - y2 != 0:  # if vertical
        for y in ranges(y1, y2):
            canvas[x1, y] += 1

    elif y1 == y2 and x1 - x2 != 0:  # if horizontal
        for x in ranges(x1, x2):
            canvas[x, y1] += 1

solution_a = len(canvas[canvas > 1])
submit(solution_a, part='a', day=DAY, year=YEAR)


# part b; use same canvas with horizontal and vertical lines already marked
for x1, y1, x2, y2 in data:
    if x1 != x2 and y1 != y2:
        for x, y in zip(ranges(x1, x2), ranges(y1, y2)):
            canvas[x, y] += 1

solution_b = len(canvas[canvas > 1])
submit(solution_b, part='b', day=DAY, year=YEAR)
