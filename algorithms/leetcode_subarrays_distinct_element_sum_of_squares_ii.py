from bisect import bisect_right
from typing import List


def sum_counts(nums: List[int]) -> int:
    mod = 1_000_000_007
    last = {}
    indices = []
    total_sum = curr = result = 0

    for i, x in enumerate(nums):
        j = last.get(x, -1)
        small = 0 if j < 0 else bisect_right(indices, j)
        large = len(indices) - small
        s = total_sum - sum(indices[:small]) if small <= large else sum(indices[small:])
        curr += 2 * (s - j * large) + i - j

        if j >= 0:
            del indices[small - 1]
            total_sum -= j

        indices.append(i)
        total_sum += i
        last[x] = i
        result += curr

    return result % mod


print(sum_counts([1, 2, 1]))
print(sum_counts([2, 2]))
