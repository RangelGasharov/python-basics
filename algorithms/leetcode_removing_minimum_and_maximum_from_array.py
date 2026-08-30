from typing import List


def minimum_deletions(nums: List[int]) -> int:
    n = len(nums)
    min_idx = nums.index(min(nums))
    max_idx = nums.index(max(nums))
    if min_idx > max_idx:
        min_idx, max_idx = max_idx, min_idx
    return min(max_idx + 1, n - min_idx, min_idx + 1 + n - max_idx)


print(minimum_deletions([2, 10, 7, 5, 4, 1, 8, 6]))
print(minimum_deletions([0, -4, 19, 1, 8, -2, -3, 5]))
print(minimum_deletions([101]))
print(minimum_deletions([0, -100000, -99998, -99999, -99997, -99996, 99999, -99995, 100000, 1]))
print(minimum_deletions([-1, -53, 93, -42, 37, 94, 97, 82, 46, 42, -99, 56, -76, -66, -67, -13, 10, 66, 85, -28]))
