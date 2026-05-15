from typing import List


def find_min(nums: List[int]) -> int:
    l = 0
    r = len(nums) - 1

    while l < r:

        mid = (l + r) // 2

        if nums[mid] < nums[r]:
            r = mid
        else:
            l = mid + 1

    return nums[l]


print(find_min([3, 4, 5, 1, 2]))
print(find_min([4, 5, 6, 7, 0, 1, 2]))
print(find_min([11, 13, 15, 17]))
