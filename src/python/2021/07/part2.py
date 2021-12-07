# Quality of life imports
from pathlib import Path
from statistics import mean
import sys

# Quality of life, define the input file location
src = Path(sys.modules['__main__'].__file__).resolve().parent
input_file_path = Path(src, "input.txt")

# Import helper functions
helper_location = Path(src, "..", "..", "helpers")
sys.path.insert(1, helper_location.as_posix())

from helpies import range_inclusive


with open(input_file_path) as f:
    pos = list(map(int, f.readline().split(',')))
    target = int(mean(pos))
    total = 0
    print(f"The mean pos is: {target}")
    for i in pos:
        dist = abs(target - i)
        area = sum(range_inclusive(1, dist))
        total += area
    print(f"The smallest amount is at pos: {target}\n\t value: {total}")
