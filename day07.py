"""Intuition for Day 07:
part a's best position is just the median
part b requires triangle sum ie the sum of the range
"""
from aocd import get_data, submit
import numpy as np

DAY = 7
YEAR = 2021

# get data
raw_data = get_data(day=DAY, year=YEAR)
data = [int(x) for x in raw_data.split(',')]

unique_positions = np.unique(data)

# part a
distance_a = sum(np.abs(data - np.median(data)))
submit(min(distance_a), part='a', day=DAY, year=YEAR)

# part b
distances_b = [sum([sum(range(d + 1)) for d in np.abs(data - position)])
               for position in unique_positions]
submit(min(distances_b), part='b', day=DAY, year=YEAR)
