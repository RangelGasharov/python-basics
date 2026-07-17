from bisect import bisect
from itertools import accumulate
from typing import List


def gcdValues(nums: List[int], queries: List[int]) -> List[int]:
    num_max = max(nums)
    freq = [0] * (num_max + 1)
    for a in nums:
        freq[a] += 1

    GCD = [0] * (num_max + 1)

    for i in range(num_max, 0, -1):
        sm = sum(freq[i::i])
        GCD[i] = sm * (sm - 1) // 2 - sum(GCD[i::i])

    GCD = list(accumulate(GCD))

    return [bisect.bisect_right(GCD, q) for q in queries]


print(gcdValues([2, 3, 4], [0, 2, 2]))
print(gcdValues([4, 4, 2, 1], [5, 3, 1, 0]))
print(gcdValues([2, 2], [0, 0]))
