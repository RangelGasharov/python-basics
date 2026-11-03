from typing import List


def min_moves(nums: List[int]) -> int:
    return max(nums) * len(nums) - sum(nums)

print(min_moves([2, 1, 3]))
print(min_moves([4, 4, 5]))