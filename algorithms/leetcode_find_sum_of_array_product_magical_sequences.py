from functools import lru_cache
import math
from typing import List

MOD = 10 ** 9 + 7


def magical_sum(m: int, k: int, nums: List[int]) -> int:
    @lru_cache(None)
    def dfs(remaining, odd_needed, index, carry):
        if remaining < 0 or odd_needed < 0 or remaining + carry.bit_count() < odd_needed:
            return 0
        if remaining == 0:
            return 1 if odd_needed == carry.bit_count() else 0
        if index >= len(nums):
            return 0

        ans = 0
        for take in range(remaining + 1):
            ways = math.comb(remaining, take) * pow(nums[index], take, MOD) % MOD
            new_carry = carry + take
            ans += ways * dfs(remaining - take, odd_needed - (new_carry % 2), index + 1, new_carry // 2)
            ans %= MOD
        return ans

    return dfs(m, k, 0, 0)


print(magical_sum(5, 5, [1, 10, 100, 10000, 1000000]))
print(magical_sum(2, 2, [5, 4, 3, 2, 1]))
print(magical_sum(1, 1, [28]))
