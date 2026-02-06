from typing import List


def min_removal(nums: List[int], k: int) -> int:
    nums.sort()
    left = 0
    max_len = 1

    for right in range(len(nums)):
        while nums[right] > k * nums[left]:
            left += 1
        max_len = max(max_len, right - left + 1)

    return len(nums) - max_len


print(min_removal([1, 2, 3, 4, 5, 6, 7], 3))
print(min_removal(
    [9514, 4037, 4183, 20670, 24972, 13008, 31534, 34223, 22722, 7793, 15527, 37410, 28870, 7506, 3485, 19748, 26934,
     333, 38955, 831, 6658, 24063, 10075, 14595, 15246, 5715, 3382, 27295, 6093, 24611, 14191, 31204, 14631, 12630], 2))
print(min_removal(
    [9514, 4037, 4183, 20670, 24972, 13008, 31534, 34223, 22722, 7793, 15527, 37410, 28870, 7506, 3485, 19748, 26934,
     333, 38955, 831, 6658, 24063, 10075, 14595, 15246, 5715, 3382, 27295, 6093, 24611, 14191, 31204, 14631, 12630],
    10))
