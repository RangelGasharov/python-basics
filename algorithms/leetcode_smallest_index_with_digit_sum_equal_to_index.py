from typing import List


def smallest_index(nums: List[int]) -> int:
    def get_digit_sum(num: int) -> int:
        digit_sum = 0
        while num > 0:
            digit_sum += num % 10
            num = num // 10
        return digit_sum

    for i in range(len(nums)):
        if get_digit_sum(nums[i]) == i:
            return i

    return -1


print(smallest_index([1, 3, 2]))
print(smallest_index([1, 10, 11]))
print(smallest_index([1, 2, 3]))
