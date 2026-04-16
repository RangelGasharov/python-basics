from bisect import bisect_left
from collections import defaultdict
from typing import List


def solveQueries(nums: List[int], queries: List[int]) -> List[int]:
    n = len(nums)
    mp = defaultdict(list)

    for i in range(n):
        mp[nums[i]].append(i)

    result = []

    for query in queries:
        positions = mp[nums[query]]

        if len(positions) == 1:
            result.append(-1)
            continue

        pos = bisect_left(positions, query)
        res = float("inf")

        left = positions[(pos - 1) % len(positions)]
        d1 = abs(query - left)
        res = min(res, min(d1, n - d1))

        right = positions[(pos + 1) % len(positions)]
        d2 = abs(query - right)
        res = min(res, min(d2, n - d2))

        result.append(res)

    return result


print(solveQueries([1, 3, 1, 4, 1, 3, 2], [0, 3, 5]))
print(solveQueries([1, 2, 3, 4], [0, 1, 2, 3]))
