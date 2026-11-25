from collections import Counter
from itertools import repeat
from operator import add, mul


def min_unique_subarray(nums: list[int]) -> int:
    n = len(nums)
    S = max(n, max(nums)) + 1

    def unique(r, k, L):
        return 1 in Counter(map(add, map(mul, r, repeat(S)), r[L - k:])).values()

    r, k = nums, 1
    if 1 in Counter(r).values():
        return 1
    while 2 * k < n:
        keys = list(map(add, map(mul, r, repeat(S)), r[k:]))
        cnt = Counter(keys)
        if 1 in cnt.values():
            break
        ids = {key: i for i, key in enumerate(cnt)}
        r, k = list(map(ids.__getitem__, keys)), 2 * k

    low, high = k + 1, min(2 * k, n)
    while low < high:
        mid = (low + high) // 2
        if unique(r, k, mid):
            high = mid
        else:
            low = mid + 1
    return low


print(min_unique_subarray([3, 3, 3]))
print(min_unique_subarray([2, 1, 2, 3, 3]))
print(min_unique_subarray([1, 1, 2, 2, 1]))
