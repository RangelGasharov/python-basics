from functools import reduce
from operator import xor
from typing import List


def xor_after_queries(nums: List[int], queries: List[List[int]]) -> int:
    mod = 10 ** 9 + 7

    for start, end, step, val in queries:
        if val == 1:
            continue

        for i in range(start, end + 1, step):
            nums[i] = (nums[i] * val) % mod

    return reduce(xor, nums)


print(xor_after_queries([1, 1, 1], [[0, 2, 1, 4]]))
print(xor_after_queries([2, 3, 1, 5, 4], [[1, 4, 2, 3], [0, 2, 1, 2]]))
