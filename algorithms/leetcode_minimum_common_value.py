from typing import List


def get_common(nums1: List[int], nums2: List[int]) -> int:
    first, second = 0, 0
    n, m = len(nums1), len(nums2)
    while first < n and second < m:
        if nums1[first] == nums2[second]:
            return nums1[first]
        if nums1[first] > nums2[second]:
            second += 1
        else:
            first += 1
    return -1


print(get_common([1, 2, 1, 2], [1]))
print(get_common([1, 2, 3], [2, 4]))
print(get_common([1, 2, 3, 6], [2, 3, 4, 5]))
