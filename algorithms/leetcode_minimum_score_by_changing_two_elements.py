from heapq import nsmallest, nlargest
from typing import List


def minimize_sum(nums: List[int]) -> int:
    a, b, c = nsmallest(3, nums)
    x, y, z = nlargest(3, nums)
    return min(x - c, z - a, y - b)


print(minimize_sum([1, 4, 7, 8, 5]))
print(minimize_sum([1, 4, 3]))
