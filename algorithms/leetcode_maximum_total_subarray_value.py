from typing import List


def max_total_value(nums: List[int], k: int) -> int:
    n_min = n_max = nums[0]

    for num in nums:
        n_min = min(n_min, num)
        n_max = max(n_max, num)

    return (n_max - n_min) * k


print(max_total_value([1, 3, 2], 2))
print(max_total_value([4, 2, 5, 1], 3))
