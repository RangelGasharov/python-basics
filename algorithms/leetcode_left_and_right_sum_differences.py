from typing import List


def left_right_difference(nums: List[int]) -> List[int]:
    right_sum = sum(nums)

    left_sum = 0
    result = []

    for num in nums:
        right_sum -= num
        result.append(abs(left_sum - right_sum))
        left_sum += num

    return result


print(left_right_difference([10, 4, 8, 3]))
