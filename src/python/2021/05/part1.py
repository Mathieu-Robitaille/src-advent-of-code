# Quality of life imports
from pathlib import Path
from sys import modules

# Quality of life, define the input file location
src = Path(modules['__main__'].__file__).resolve().parent
input_file_path = Path(src, "input.txt")

def check_spot(x, y, board):
    if (x, y) in board:
        # If its in the board already its an overlap
        board[(x, y)] = 1
    else:
        board[(x, y)] = 0

def range_inclusive(start, end):
    return range(start, end + 1)

def generate_points(x1, y1, x2, y2, board):
    if x1 == x2:
        x = [x1]
        y = list(range_inclusive(*sorted([y1, y2])))
        for i in x:
            for j in y:
                check_spot(i, j, board)
    elif y1 == y2:
        y = [y1]
        x = list(range_inclusive(*sorted([x1, x2])))
        for i in x:
            for j in y:
                check_spot(i, j, board)
    


input, board = [], {}
with open(input_file_path) as f:
    while (inp := f.readline().rstrip()) != "":
        pos = list(map(int, inp.replace(' -> ', ',').split(',')))
        generate_points(pos[0], pos[1], pos[2], pos[3], board)


print(sum(board.values()))
# Fuck diags for now eh?


