from typing import List


def unique_xor_triplets(nums: List[int]) -> int:
    MAX_XOR = 2048

    pair_xor = [False] * MAX_XOR
    triplet_xor = [False] * MAX_XOR

    n = len(nums)

    for i in range(n):
        for j in range(i, n):
            pair_xor[nums[i] ^ nums[j]] = True

    for x in range(MAX_XOR):
        if not pair_xor[x]:
            continue

        for v in nums:
            triplet_xor[x ^ v] = True

    return sum(triplet_xor)


print(unique_xor_triplets([1, 3]))
print(unique_xor_triplets([6, 7, 8, 9]))
