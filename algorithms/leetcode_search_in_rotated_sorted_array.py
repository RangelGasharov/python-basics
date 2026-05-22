from typing import List


def search(nums: List[int], target: int) -> int:
    n = len(nums)
    l, r = 0, n - 1
    m = (l + r) // 2

    while l <= r:
        m = (l + r) // 2
        if nums[m] == target:
            return m
        elif nums[l] <= nums[m]:
            if nums[l] <= target <= nums[m]:
                r = m - 1
            else:
                l = m + 1
        else:
            if nums[m] <= target <= nums[r]:
                l = m + 1
            else:
                r = m - 1

    if nums[m] != target:
        return -1

    return m


print(search([4, 5, 6, 7, 0, 1, 2], 0))
print(search([4, 5, 6, 7, 0, 1, 2], 3))
print(search([1], 0))
print(search([5, 1, 3], 0))
