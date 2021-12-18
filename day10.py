from aocd import get_data, submit
from aocd.transforms import lines
import numpy as np

DAY = 10
YEAR = 2021

raw_data = get_data(day=DAY, year=YEAR)
data = lines(raw_data)

OPENING = list('{([<')

CLOSING = {'{': '}',
           '(': ')',
           '[': ']',
           '<': '>'}

# part a
SCORING_A = {')': 3,
             ']': 57,
             '}': 1197,
             '>': 25137}
# part b
SCORING_B = {')': 1,
             ']': 2,
             '}': 3,
             '>': 4}

score_a = 0
line_scores = []
for line in data:
    corrupt = False
    tracker = []
    for char in list(line):
        if char in OPENING:
            tracker.append(char)
        elif CLOSING[tracker.pop(-1)] != char:
            score_a += SCORING_A[char]  # part a
            corrupt = True
            break

    if not corrupt:  # part b
        line_score = 0
        while len(tracker) > 0:
            line_score = line_score * 5 + SCORING_B[CLOSING[tracker.pop(-1)]]
        line_scores.append(line_score)

# submit(score_a, part='a', day=DAY, year=YEAR)

score_b = sorted(line_scores)[len(line_scores) // 2]
# submit(score, part='b', day=DAY, year=YEAR)


# test
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
        if char in OPENING:
            tracker.append(char)
        else:
            tracker.pop(-1)
    while len(tracker) > 0:
        line_score = line_score * 5 + SCORING_B[CLOSING[tracker.pop(-1)]]
    scores.append(line_score)
print(np.median(scores))
