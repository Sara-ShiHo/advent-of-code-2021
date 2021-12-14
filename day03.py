from aocd import get_data
from aocd.transforms import lines
from aocd import submit
import collections

DAY = 3
YEAR = 2021

# get data
raw_data = get_data(day=DAY, year=YEAR)
data = lines(raw_data)


# part a
def solution(data, rate):
    n = len(data[0])
    binary_result = ''
    for i in range(n):
        column = [int(line[i]) for line in data]
        counter = collections.Counter(column)
        if rate.lower() == 'gamma':
            rank = 0
        elif rate.lower() == 'epsilon':
            rank = -1
        binary_result += str(counter.most_common()[rank][0])
    return int(binary_result, 2)


gamma = solution(data, 'gamma')
epsilon = solution(data, 'epsilon')
submit(gamma * epsilon, part="a", day=DAY, year=YEAR)


# part a
def solution(data, rate):
    n = len(data[0])
    binary_result = ''
    for i in range(n):
        column = [int(line[i]) for line in data]
        counter = collections.Counter(column)
        frequency = counter.most_common()
        if rate.lower() == 'oxy':
            if len(frequency) == 2 and frequency[0][1] == frequency[1][1]:
                result = '1'  # handle tie
            else:
                result = str(frequency[0][0]) # most frequent

        elif rate.lower() == 'co2':
            if len(frequency) == 2 and frequency[0][1] == frequency[1][1]:
                result = '0'  # handle tie
            else:
                result = str(frequency[-1][0]) # least frequent

        binary_result += result
        data = [line for line in data if line[i] == result]
    return int(binary_result, 2)


oxy = solution(data, 'oxy')
co2 = solution(data, 'co2')
submit(oxy * co2, part="b", day=DAY, year=YEAR)
