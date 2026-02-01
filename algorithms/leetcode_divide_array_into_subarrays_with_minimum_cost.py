from typing import List


def minimum_cost(nums: List[int]) -> int:
    first = nums[1]
    second = max(nums[1], nums[2])
    for i in range(2, len(nums)):
        if nums[i] < first:
            second = first
            first = nums[i]
        elif nums[i] < second:
            second = nums[i]
    return nums[0] + first + second


print(minimum_cost([1, 2, 3, 12, 5, 4, 3, 10, 3, 1, 1, 1, 2, 3, 12, 5, 4, 3, 10, 3, 1, 1]))
print(minimum_cost([10, 3, 1, 1]))
print(minimum_cost([1, 2, 3, 12]))
print(minimum_cost([5, 4, 3]))
print(minimum_cost([1, 1, 1, 1, 1]))
