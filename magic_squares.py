import random
import numpy as np

# These matrices all have diagonals which add up to 1 as well has having the property that permutation matrices have
# This smol script is obviously only useful for 4 x 4 magic squares
acceptable_matrices = [
  [
    [1, 0, 0, 0],
    [0, 0, 0, 1],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
  ],
  [
    [0, 0, 1, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [1, 0, 0, 0],
  ],
  [
    [1, 0, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [0, 1, 0, 0],
  ],
  [
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0],
    [1, 0, 0, 0],
  ],
  [
    [0, 0, 1, 0],
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
  ],
  [
    [0, 0, 0, 1],
    [0, 1, 0, 0],
    [1, 0, 0, 0],
    [0, 0, 1, 0],
  ],
  [
    [0, 0, 0, 1],
    [1, 0, 0, 0],
    [0, 0, 1, 0],
    [0, 1, 0, 0],
  ],
  [
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 0],
    [0, 0, 0, 1],
  ]
]

# this just makes adding them up more convenient
acceptable_matrices = [np.array(matrix) for matrix in acceptable_matrices]

magic_square = np.zeros((4, 4))
for i in range(int(input("Give a value for k: \n"))):
  perm_mat = random.choice(acceptable_matrices)
  magic_square += perm_mat
print(magic_square)
