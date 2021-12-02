# Quality of life imports
from pathlib import Path
from sys import modules
from itertools import tee, islice

# Quality of life, define the input file location
src = Path(modules['__main__'].__file__).resolve().parent
input_file_path = Path(src, "input.txt")

bs = 2

print(len([a for a, b in list(zip(*[islice(open(input_file_path, "r").read().split(), x, None) for x in range(bs)])) if int(b) > int(a)]))

