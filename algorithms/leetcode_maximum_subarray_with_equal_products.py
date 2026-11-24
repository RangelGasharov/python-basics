from fractions import gcd
from typing import List


def max_length(nums: List[int]) -> int:
    best, left, product = 2, 0, 1
    for right, x in enumerate(nums):
        while gcd(product, x) > 1:
            product //= nums[left]
            left += 1
        product *= x
        best = max(best, right - left + 1)
    return best


print(max_length([1, 2, 1, 2, 1, 1, 1]))
print(max_length([2, 3, 4, 5, 6]))
print(max_length([1, 2, 3, 1, 4, 5, 1]))
