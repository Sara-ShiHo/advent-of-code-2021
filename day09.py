from aocd import get_data, submit
from aocd.transforms import lines
import numpy as np

DAY = 9
YEAR = 2021

# get data
raw_data = get_data(day=DAY, year=YEAR)
data = [[int(num) for num in list(line)] for line in lines(raw_data)]
data = np.array(data)
data = data[0:10, 0:10]
print(data)


# part a
left_right = data[:, :-1] - data[:, 1:]
left_right = np.concatenate((np.ones((len(data), 1)), left_right), 1)

right_left = data[:, 1:] - data[:, :-1]
right_left = np.concatenate((right_left, np.ones((len(data), 1))), 1)

up_down = data[:-1, :] - data[1:, :]
up_down = np.concatenate((np.ones((1, len(data[0]))), up_down), 0)

down_up = data[1:, :] - data[:-1, :]
down_up = np.concatenate((down_up, np.ones((1, len(data[0])))), 0)

horizontal = np.logical_and(left_right > 0, right_left > 0)
vertical = np.logical_and(up_down > 0, down_up > 0)
low_points = data[np.logical_and(horizontal, vertical)]

solution_a = sum(low_points) + len(low_points)
# submit(solution_a, part='a', day=DAY, year=YEAR)

# part b
print(np.logical_and(np.abs(left_right) == 1, np.abs(right_left) == 1))
