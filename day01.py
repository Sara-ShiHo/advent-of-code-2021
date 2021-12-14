"""Intuition for Day 01:
Calculate difference between the data starting from the second position and
the data ending at the second-to-last position. Count the positive differences.
"""
from aocd import get_data
from aocd.transforms import numbers
from aocd import submit

DAY = 1
YEAR = 2021

# get data
raw_data = get_data(day=DAY, year=YEAR)
data = numbers(raw_data)


# general solution
def count_increases(data):
    diff = [y - x for x, y in zip(data[:len(data)-1],
                                  data[1:])]
    increases = sum([1 for x in diff if x > 0])
    return increases

# part a
solution_a = count_increases(data)
submit(solution_a, part="a", day=DAY, year=YEAR)

# part b
window_sum = [x + y + z
              for x, y, z in zip(data[:len(data)-2],
                                 data[1:len(data)-1],
                                 data[2:])]
solution_b = count_increases(window_sum)
submit(solution_b, part="b", day=DAY, year=YEAR)
