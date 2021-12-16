"""Intuition for Day 06:
The intuitive solution - growing an array - is not scalable for 256 days
For part b, keep track of counts in a dictionary instead of using an array.
"""
from collections import Counter

from aocd import get_data, submit
import numpy as np

DAY = 6
YEAR = 2021

# get data
raw_data = get_data(day=DAY, year=YEAR)
data = np.array([int(x) for x in raw_data.split(',')])

day = 0
while day < 80:
    n_reset = len(data[data == 0])
    data[data == 0] = 6 + 1
    data = np.append(data, [8+1] * n_reset)
    data -= 1
    day += 1

submit(len(data), part='a', day=DAY, year=YEAR)


# part b requires different approach
# don't reset data or start from 0
counts = dict(Counter(data))
while day < 256:
    temp_counts = {}
    for i in range(0, 8):
        temp_counts[i] = counts[i + 1]

    temp_counts[8] = counts[0]
    temp_counts[6] += counts[0]

    counts = temp_counts
    day += 1

solution_b = sum(counts.values())
submit(solution_b, part='b', day=DAY, year=YEAR)
