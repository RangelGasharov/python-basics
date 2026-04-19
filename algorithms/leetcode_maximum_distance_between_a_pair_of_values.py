from bisect import bisect_left
from typing import List


def maxDistance(nums1: List[int], nums2: List[int]) -> int:
    i = j = max_distance = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            max_distance = max(max_distance, j - i)
            j += 1
        else:
            i += 1
    return max_distance


print(maxDistance([55, 30, 5, 4, 2], [100, 20, 10, 10, 5]))
print(maxDistance([2, 2, 2], [10, 10, 1]))
print(maxDistance([30, 29, 19, 5], [25, 25, 25, 25, 25]))
