from typing import List


def missing_integer(nums: List[int]) -> int:
    prefix_sum = 0
    n = len(nums)
    seen = set(nums)

    if n == 1:
        return nums[0] + 1

    for i in range(1, n):
        prefix_sum += nums[i - 1]
        if nums[i - 1] + 1 != nums[i]:
            break
        if i == n - 1:
            prefix_sum += nums[i]

    while prefix_sum in seen:
        prefix_sum += 1

    return prefix_sum


print(missing_integer([1, 2, 3, 2, 5]))
print(missing_integer([3, 4, 5]))
print(missing_integer([3, 4, 5, 1, 12, 14, 13]))
print(missing_integer([8, 9, 10, 10, 7, 8]))
print(missing_integer([14]))
