from typing import List


def min_swaps(nums: List[int]) -> int:
    digit_sum = lambda x: sum(map(int, str(x)))
    rank = {x: k for k, x in enumerate(sorted(nums, key=lambda x: (digit_sum(x), x)))}
    home = [rank[x] for x in nums]

    swaps = 0
    for i in range(len(home)):
        while home[i] != i:
            j = home[i]
            home[i], home[j] = home[j], home[i]
            swaps += 1

    return swaps


print(min_swaps([37, 100]))
print(min_swaps([22, 14, 33, 7]))
print(min_swaps([18, 43, 34, 16]))
