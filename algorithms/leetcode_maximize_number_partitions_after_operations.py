from functools import lru_cache


def max_partitions_after_operations(s: str, k: int) -> int:
    count = [1 << (ord(i) - ord("a")) for i in s]

    @lru_cache(None)
    def dp(i, j, mask):
        if i == len(count):
            return 0
        mask2 = mask | count[i]
        if mask2.bit_count() > k:
            result = 1 + dp(i + 1, j, count[i])
        else:
            result = dp(i + 1, j, mask2)
        if j:
            for q in range(26):
                mask2 = mask | (1 << q)
                if mask2.bit_count() > k:
                    result = max(result, 1 + dp(i + 1, 0, 1 << q))
                else:
                    result = max(result, dp(i + 1, 0, mask2))
        return result

    return dp(0, 1, 0) + 1


print(max_partitions_after_operations("accca", 2))
print(max_partitions_after_operations("aabaab", 3))
print(max_partitions_after_operations("xxyz", 1))
