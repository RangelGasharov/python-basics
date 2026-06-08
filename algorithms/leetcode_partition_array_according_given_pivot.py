from typing import List


def pivot_array(self, nums: List[int], pivot: int) -> List[int]:
    n = len(nums)
    if n == 1:
        return nums
    r = []
    l, m = 0, 0
    for x in nums:
        if x < pivot:
            nums[l] = x
            l += 1
        elif x > pivot:
            r.append(x)
        else:
            m += 1
    return nums[:l] + [pivot] * m + r
