from aocd import get_data, submit
from aocd.transforms import lines
import numpy as np

DAY = 10
YEAR = 2021

raw_data = get_data(day=DAY, year=YEAR)
data = lines(raw_data)

opening = list('{([<')
closing = {'{': '}',
           '(': ')',
           '[': ']',
           '<': '>'}

# part a
scoring = {')': 3,
           ']': 57,
           '}': 1197,
           '>': 25137}

score = 0
tracker = []
corrupt_indices = []
new_data = []
for i, line in enumerate(data):
    for char in line:
        if char in opening:
            tracker.append(char)
        else:
            if closing[tracker.pop(-1)] != char:
                score += scoring[char]
                corrupt_indices.append(i)
                break
# submit(score, part='a', day=DAY, year=YEAR)

# part b
scoring = {')': 1,
           ']': 2,
           '}': 3,
           '>': 4}

data = [line for i, line in enumerate(data) if i not in corrupt_indices].copy()
scores = []
for line in data:
    items = list(line)
    tracker = []
    line_score = 0
    while len(items) > 0:
        char = items.pop(0)
        if char in opening:
            tracker.append(char)
        else:
            tracker.pop(-1)
    while len(tracker) > 0:
        line_score = line_score * 5 + scoring[closing[tracker.pop(-1)]]
    scores.append(line_score)
print(np.median(scores))
# submit(np.median(scores), part='b', day=DAY, year=YEAR)

# check
scores = []
for line in ['[({(<(())[]>[[{[]{<()<>>',
             '[(()[<>])]({[<{<<[]>>(',
             '(((({<>}<{<{<>}{[]{[]{}',
             '{<[[]]>}<{[{[{[]{()[[[]',
             '<{([{{}}[<[[[<>{}]]]>[]]']:
    items = list(line)
    tracker = []
    line_score = 0
    while len(items) > 0:
        char = items.pop(0)
        if char in opening:
            tracker.append(char)
        else:
            tracker.pop(-1)
    while len(tracker) > 0:
        line_score = line_score * 5 + scoring[closing[tracker.pop(-1)]]
    scores.append(line_score)
print(np.median(scores))
