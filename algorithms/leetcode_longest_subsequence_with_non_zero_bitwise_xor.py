from typing import List


def longest_subsequence(nums: List[int]) -> int:
    n = len(nums)
    if [0] * n == nums:
        return 0

    total = 0

    for num in nums:
        total ^= num
    return n if total else n - 1


print(longest_subsequence([1, 2, 3]))
print(longest_subsequence([2, 3, 4]))
print(longest_subsequence([0, 0, 0]))
