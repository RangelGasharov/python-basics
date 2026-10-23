from typing import List


def sort_permutation(nums: List[int]) -> int:
    k = -1
    for i, x in enumerate(nums):
        if x != i:
            k &= x
            if not k:
                return 0
    return max(k, 0)


print(sort_permutation([0, 3, 2, 1]))
print(sort_permutation([0, 1, 3, 2]))
print(sort_permutation([3, 2, 1, 0]))
