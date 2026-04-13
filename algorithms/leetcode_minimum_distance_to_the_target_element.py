from typing import List


def get_min_distance(nums: List[int], target: int, start: int) -> int:
    left = start
    right = start
    while True:
        if left >= 0:
            if nums[left] == target:
                return start - left
        if right < len(nums):
            if nums[right] == target:
                return right - start
        left -= 1
        right += 1


print(get_min_distance([1, 2, 3, 4, 5], 5, 3))
print(get_min_distance([1], 1, 0))
print(get_min_distance([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 1, 0))
print(get_min_distance([5, 3, 6], 5, 2))
print(get_min_distance([5, 3, 5, 6], 5, 2))
