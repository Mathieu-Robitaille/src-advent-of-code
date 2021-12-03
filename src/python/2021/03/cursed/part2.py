# Quality of life imports
from pathlib import Path
from sys import modules

# Quality of life, define the input file location
src = Path(modules['__main__'].__file__).resolve().parent
input_file_path = Path(src, "..", "input.txt")


with open(input_file_path.as_posix()) as f:

    # Read 2 lines for testing
    test = [f.readline().split() for x in range(2)]

