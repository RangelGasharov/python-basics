from collections import defaultdict
from typing import List


def max_subarray_length(nums: List[int], k: int) -> int:
    count = 0
    freq = defaultdict(int)
    l = 0

    for r, num in enumerate(nums):
        freq[num] += 1
        while freq[num] > k:
            freq[nums[l]] -= 1
            l += 1
        count = max(count, r - l + 1)
    return count


print(max_subarray_length([1, 2, 3, 1, 2, 3, 1, 2], 2))
print(max_subarray_length([1, 2, 1, 2, 1, 2, 1, 2], 1))
print(max_subarray_length([5, 5, 5, 5, 5, 5, 5], 4))
