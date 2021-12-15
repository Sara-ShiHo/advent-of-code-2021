from aocd import get_data
from aocd.transforms import lines
from aocd import submit
import numpy as np

DAY = 4
YEAR = 2021

# get data
raw_data = get_data(day=DAY, year=YEAR)
data = lines(raw_data)

# format data
calls = [int(num) for num in data[0].split(',')]

boards = []
board = []
for line in data[2:]:
    if line == '':
        boards.append(np.array(board))
        board = []
    else:
        board.append([int(num) for num in line.split()])
boards = np.array(boards)

# run solution for both a and b
winners = []
for call in calls:
    boards[boards == call] = 0
    # sum columns and rows
    assess = [(min(np.sum(board, axis=0)),
               min(np.sum(board, axis=1)))
              for board in boards]
    winners = [(i, total)
               for i, total in enumerate(assess)
               if 0.0 in total]

    # one board has won (part a)
    if len(winners) == 1:
        winning_board = boards[winners[0][0]].copy()
        winning_call = call

    # there is only one board left (part b). record who it is.
    if len(winners) == len(boards) - 1:
        last_winner = [(i, total) for i, total in enumerate(assess)
                       if 0.0 not in total]

    # there are no more boards left. record the last board's winning state.
    if len(winners) == len(boards):
        last_board = boards[last_winner[0][0]].copy()
        last_call = call
        break

submit(np.sum(winning_board) * winning_call, part='a', day=DAY, year=YEAR)
submit(np.sum(last_board) * last_call, part='b', day=DAY, year=YEAR)
