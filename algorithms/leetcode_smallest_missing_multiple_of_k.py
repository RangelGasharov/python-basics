from typing import List


def missing_multiple(nums: List[int], k: int) -> int:
    seen = set()

    for num in nums:
        seen.add(num)

    i = k
    while i in seen:
        i += k

    return i


print(missing_multiple([8, 2, 3, 4, 6], 2))
print(missing_multiple([1, 4, 7, 10, 15], 5))
