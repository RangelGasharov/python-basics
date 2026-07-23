from typing import List


def unique_xor_triplets(nums: List[int]) -> int:
    n = len(nums)
    if n <= 2:
        return n
    m = -1
    for i in range(32):
        if n & (1 << i) != 0:
            m = i
    return 1 << (m + 1)


print(unique_xor_triplets([1, 2]))
print(unique_xor_triplets([3, 1, 2]))
