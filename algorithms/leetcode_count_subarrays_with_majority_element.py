from typing import List


def count_majority_subarrays(nums: List[int], target: int) -> int:
    n = len(nums)
    pre = [0] * (2 * n + 1)

    pre[n] = 1

    count = n
    pre_sum = 0
    result = 0

    for x in nums:
        if x == target:
            pre_sum += pre[count]

            count += 1
            pre[count] += 1
        else:
            count -= 1

            pre_sum -= pre[count]
            pre[count] += 1

        result += pre_sum

    return result


print(count_majority_subarrays([1, 2, 2, 3], 2))
print(count_majority_subarrays([1, 1, 1, 1], 1))
print(count_majority_subarrays([1, 2, 3], 4))
