from typing import List


def max_rotate_function(nums: List[int]) -> int:
    total_sum = sum(nums)
    n = len(nums)
    current = 0

    for i in range(n):
        current += nums[i] * i

    max_value = current

    for i in range(1, n):
        current = current + total_sum - n * nums[n - i]
        if current > max_value:
            max_value = current

    return max_value


print(max_rotate_function([1, 2, 3, 4]))
print(max_rotate_function([4, 3, 2, 6]))
print(max_rotate_function([100]))
print(max_rotate_function([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
