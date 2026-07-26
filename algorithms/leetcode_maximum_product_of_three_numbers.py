from typing import List


def maximum_product(nums: List[int]) -> int:
    a, b, c = -float("inf"), -float("inf"), -float("inf")
    d, e = float("inf"), float("inf")

    for num in nums:
        if num > a:
            a, b, c = num, a, b
        elif num > b:
            b, c = num, b
        elif num > c:
            c = num

        if num < d:
            d, e = num, d
        elif num < e:
            e = num
    return max(a * b * c, a * d * e)


print(maximum_product([1, 2, 3]))
print(maximum_product([1, 2, 3, 4]))
print(maximum_product([-1, -2, -3]))
print(maximum_product([-3, 3, -3, 2, 2]))
