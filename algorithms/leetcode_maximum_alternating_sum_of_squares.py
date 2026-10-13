from typing import List

import numpy as np


def max_alternating_sum(nums: List[int]) -> int:
    squares = np.square(np.asarray(nums, dtype=np.int64))
    h = len(squares) // 2
    squares.partition(h)
    return int(squares.sum() - 2 * squares[:h].sum())


print(max_alternating_sum([1, 2, 3]))
print(max_alternating_sum([1, -1, 2, -2, 3, -3]))
