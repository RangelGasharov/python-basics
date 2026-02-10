from typing import List


def longest_balanced(self, nums: List[int]) -> int:
    max_len = 0
    n = len(nums)

    for start in range(n):
        evens = set()
        odds = set()
        for end in range(start, n):
            if nums[end] % 2 == 0:
                evens.add(nums[end])
            else:
                odds.add(nums[end])

            if len(evens) == len(odds):
                max_len = max(max_len, end - start + 1)

    return max_len


print(longest_balanced([4, 3, 2, 1]))
print(longest_balanced([2, 5, 4, 3]))
print(longest_balanced([3, 2, 2, 5, 4]))
print(longest_balanced([1, 2, 3, 2]))
print(longest_balanced([6, 6]))
