from typing import List


def max_product(nums: List[int]) -> int:
    a = b = 0

    for num in nums:
        if num > a:
            a, b = num, a
        elif num > b:
            b = num

    return (a - 1) * (b - 1)


print(max_product([3, 4, 5, 2]))
print(max_product([1, 5, 4, 5]))
print(max_product([3, 7]))
