from typing import List


def max_sum(nums: List[int], k: int) -> int:
    bits = [0] * 30
    result = 0
    mod = 1000000007

    for x in nums:
        for i in range(30):
            if x & (1 << i):
                bits[i] += 1

    for _ in range(k):
        x = 0
        for i in range(30):
            if bits[i] > 0:
                x |= 1 << i
                bits[i] -= 1
        result = (result + x * x) % mod

    return result


print(max_sum([2, 6, 5, 8], 2))
print(max_sum([4, 5, 4, 7], 3))
