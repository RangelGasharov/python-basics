from typing import List


def max_value(nums: List[int]) -> List[int]:
    n = len(nums)

    prefix = [0] * n
    sufix = [0] * n
    result = [0] * n

    prefix[0] = nums[0]
    for i in range(1, n):
        prefix[i] = max(prefix[i - 1], nums[i])

    sufix[-1] = nums[-1]
    for i in range(n - 2, -1, -1):
        sufix[i] = min(sufix[i + 1], nums[i])

    result[-1] = prefix[-1]

    for i in range(n - 2, -1, -1):

        if prefix[i] > sufix[i + 1]:
            result[i] = result[i + 1]

        else:
            result[i] = prefix[i]

    return result


print(max_value([2, 1, 3]))
print(max_value([2, 3, 1]))
