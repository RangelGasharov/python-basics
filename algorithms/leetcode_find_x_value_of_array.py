from itertools import groupby
from typing import List


def result_array(nums: List[int], k: int) -> List[int]:
    n = len(nums)

    if k == 1:
        return [n * (n + 1) // 2]

    nums = [num % k for num in nums]

    if k == 2:
        groups = groupby(nums)
        counts = [len(list(group)) for key, group in groups if key != 0]
        odds = sum(c * (c + 1) for c in counts) // 2
        return [(n * (n + 1)) // 2 - odds, odds]

    result, counter, prev_count = [0] * k, [0] * k, [0] * k

    for num in nums:
        counter[num] += 1

        for i in range(k):
            counter[(num * i) % k] += prev_count[i]

        for i in range(k):
            result[i] += counter[i]

        prev_count, counter = counter, [0] * k

    return result


print(result_array([1, 2, 3, 4, 5], 3))
print(result_array([1, 2, 4, 8, 16, 32], 4))
print(result_array([1, 1, 2, 1, 1], 2))
