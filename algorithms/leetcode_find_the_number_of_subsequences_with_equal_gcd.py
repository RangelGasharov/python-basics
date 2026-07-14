from fractions import gcd
from functools import lru_cache
from typing import List


def subsequence_pair_count(nums: List[int]):
    mod = 10 ** 9 + 7
    n = len(nums)

    @lru_cache(None)
    def solve(index, group1, group2):
        if index == n:
            return 1 if group1 != 0 and group1 == group2 else 0

        result = solve(index + 1, group1, group2)

        seq1 = nums[index] if group1 == 0 else gcd(group1, nums[index])
        result = (result + solve(index + 1, seq1, group2)) % mod

        seq2 = nums[index] if group2 == 0 else gcd(group2, nums[index])
        result = (result + solve(index + 1, group1, seq2)) % mod

        return result

    return solve(0, 0, 0)


print(subsequence_pair_count([1, 2, 3, 4]))
print(subsequence_pair_count([10, 20, 30]))
print(subsequence_pair_count([1, 1, 1, 1]))
