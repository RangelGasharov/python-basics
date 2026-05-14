from typing import List


def is_good(nums: List[int]) -> bool:
    n = len(nums) - 1
    seen = set()
    dup = False

    for num in nums:
        if num > n: return False

        if num in seen:
            if num < n or dup: return False
            dup = True
            continue

        seen.add(num)

    return True


print(is_good([2, 1, 3]))
print(is_good([1, 3, 3, 2]))
print(is_good([1, 1]))
print(is_good([3, 4, 4, 1, 2, 1]))
