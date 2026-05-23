from typing import List


def check(nums: List[int]) -> bool:
    is_rotated = False

    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            if nums[len(nums) - 1] > nums[0] or is_rotated:
                return False
            is_rotated = True
    return True


print(check([3, 4, 5, 1, 2]))
print(check([2, 1, 3, 4]))
print(check([1, 2, 3]))
print(check([6, 7, 2, 7, 5]))
print(check([7, 9, 1, 1, 1, 3]))
