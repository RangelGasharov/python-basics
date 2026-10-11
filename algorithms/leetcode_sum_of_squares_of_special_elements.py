from typing import List


def sum_of_squares(nums: List[int]) -> int:
    total = 0
    n = len(nums)
    for i in range(n):
        num = nums[i]

        if n % (i + 1) == 0:
            total += num * num

    return total


print(sum_of_squares([1, 2, 3, 4]))
print(sum_of_squares([2, 7, 1, 19, 18, 3]))
