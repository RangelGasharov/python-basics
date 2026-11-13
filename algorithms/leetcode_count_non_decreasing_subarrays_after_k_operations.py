from collections import deque
from typing import List


def count_non_decreasing_subarrays(nums: List[int], k: int) -> int:
    starts = deque()
    result, water, r = 0, 0, len(nums) - 1

    for l in reversed(range(len(nums))):
        x = nums[l]
        while starts and nums[starts[0]] <= x:
            s = starts.popleft()
            end = starts[0] if starts else r + 1
            water += (x - nums[s]) * (end - s)
        starts.appendleft(l)
        while water > k:
            water -= nums[starts[-1]] - nums[r]
            if starts[-1] == r:
                starts.pop()
            r -= 1
        result += r - l + 1
    return result


print(count_non_decreasing_subarrays([6, 3, 1, 2, 4, 4], 7))
print(count_non_decreasing_subarrays([6, 3, 1, 3, 6], 4))
