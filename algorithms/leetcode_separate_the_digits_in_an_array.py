from typing import List


def separate_digits(nums: List[int]) -> List[int]:
    result = []
    for i in range(len(nums) - 1, -1, -1):
        num = nums[i]

        while num > 0:
            result.append(num % 10)
            num //= 10
    result.reverse()
    return result


print(separate_digits([1234, 56, 7]))
print(separate_digits([13, 25, 83, 77]))
print(separate_digits([7, 1, 3, 9]))
