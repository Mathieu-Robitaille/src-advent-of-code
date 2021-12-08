# Quality of life imports
from pathlib import Path
from sys import modules

# Quality of life, define the input file location
src = Path(modules['__main__'].__file__).resolve().parent
input_file_path = Path(src, "input.txt")

num_segments = {
    2: 1,
    3: 7,
    4: 4,
    5: [2, 5],
    6: [0, 3, 6, 9],
    7: 8
}

# One is the only one with 2 segments, we can validate 2 and 5 with them and 7
# 2 will share with 7(a, c) and 1(c),
# 5 will share with 7(a) and 1(f)

# 3 Will share with 7(a, c, f), 1(c, f), 2 & 5 (a, d, g)


#  aaaa 
# b    c
# b    c
#  dddd 
# e    f
# e    f
#  gggg 


with open(input_file_path) as f:
    pass
