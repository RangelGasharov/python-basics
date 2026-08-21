import math
from itertools import combinations
from typing import List


def findKthSmallest(coins: List[int], k: int) -> int:
    n = len(coins)
    upper = min(coins) * k

    terms = []
    for r in range(1, n + 1):
        sign = 1 if r & 1 else -1
        for subset in combinations(coins, r):
            l = math.lcm(*subset)
            if l <= upper:
                terms.append((l, sign))

    def count(x: int) -> int:
        total = 0
        for l, sign in terms:
            total += sign * (x // l)
        return total

    left = 1
    right = min(coins) * k

    while left < right:
        middle = left + (right - left) // 2
        if count(middle) >= k:
            right = middle
        else:
            left = middle + 1
    return left


print(findKthSmallest([3, 6, 9], 3))
print(findKthSmallest([5, 2], 7))
print(findKthSmallest([5, 2, 3, 6, 9, 17, 19, 25, 8, 10, 11], 3194712948))
