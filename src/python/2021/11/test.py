# Quality of life imports
from pathlib import Path
from sys import modules
from typing import Tuple

# OH SHIT ITS THAT BOY
import numpy as np

# Quality of life, define the input file location
src = Path(modules['__main__'].__file__).resolve().parent
input_file_path = Path(src, "ex2.txt")


def create_increase_matrix(index, shape=(10, 10)):
    
    # Matrix representing the modification to the base matrix
    a = np.ones((3, 3))
    a[1][1] = 0
    
    # now we need to pad it with zeros until a[1][1] is at the index location

    top = index[0]
    right = shape[1] - 1 - index[1]
    bottom = shape[0] - 1 - index[0]
    left = index[1]
    return np.array([x[1:-1] for x in np.pad(a, ((top, bottom), (left, right)), "constant")[1:-1]])

shape = (10, 10)

print(matrix := create_increase_matrix([0, 2], shape))
print(matrix.shape == shape)
print(matrix.shape)
input()

