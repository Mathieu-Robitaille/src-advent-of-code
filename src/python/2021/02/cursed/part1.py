# Quality of life imports
from functools import reduce
from pathlib import Path
from sys import modules

# Quality of life, define the input file location
src = Path(modules['__main__'].__file__).resolve().parent
input_file_path = Path(src, "..", "input.txt")

def f(b):
    return int(b[b.find(''):])

x = lambda b : f(b) if b[0] == "d" else 0
u = lambda b : -f(b) if b[0] == "u" else 0
y = lambda b : f(b) if b[0] == "f" else 0
s = sum

with open(input_file_path) as f:
    i = [_.rstrip() for _ in f.readlines()]
    d = [list(map(_, i)) for _ in [x, u, y]]
    print(f"The total dist is:", s(s(_) for _ in d[:-1]) * s(d[-1]))
