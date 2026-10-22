from typing import List


def min_operations(nums: List[int]) -> int:
    n = len(nums)
    start = nums[0]

    if nums == [*range(start, n), *range(start)]:
        return 0 if start == 0 else min(n - start, start + 2)

    if nums == [*range(start, -1, -1), *range(n - 1, start, -1)]:
        num = nums[-1]
        return min(n - num, num) + 1

    return -1


print(min_operations([0, 2, 1]))
print(min_operations([1, 0, 2]))
print(min_operations([2, 0, 1, 3]))
