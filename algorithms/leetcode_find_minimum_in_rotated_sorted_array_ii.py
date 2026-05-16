from bisect import bisect_left
from typing import List


def find_min(nums: List[int]) -> int:
    while len(nums) > 1 and nums[-1] == nums[0]:
        nums.pop()

    return nums[bisect_left(nums, True, key=lambda n: n <= nums[-1])]


print(find_min([1, 3, 5]))
print(find_min([2, 2, 2, 0, 1]))
