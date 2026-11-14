from typing import List

from sortedcontainers import SortedList


def minimum_sum_subarray(nums: List[int], l: int, r: int) -> int:
    n = len(nums)
    pre = [0] * (n + 1)
    for i in range(n):
        pre[i + 1] = pre[i] + nums[i]

    window = SortedList()
    best = float("inf")

    for j in range(l, n + 1):
        window.add(pre[j - l])
        if j - r - 1 >= 0:
            window.remove(pre[j - r - 1])

        k = window.bisect_left(pre[j])
        if k > 0:
            best = min(best, pre[j] - window[k - 1])

    return best if best != float("inf") else -1


print(minimum_sum_subarray([3, -2, 1, 4], 2, 3))
print(minimum_sum_subarray([-2, 2, -3, 1], 2, 3))
print(minimum_sum_subarray([1, 2, 3, 4], 2, 4))
