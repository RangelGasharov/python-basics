from typing import List


def max_distance(nums1: List[int], nums2: List[int]) -> int:
    i = j = max_dist = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            max_dist = max(max_dist, j - i)
            j += 1
        else:
            i += 1
    return max_dist


print(max_distance([55, 30, 5, 4, 2], [100, 20, 10, 10, 5]))
print(max_distance([2, 2, 2], [10, 10, 1]))
print(max_distance([30, 29, 19, 5], [25, 25, 25, 25, 25]))
