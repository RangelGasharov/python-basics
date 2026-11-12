from typing import List


def longest_monotonic_subarray(nums: List[int]) -> int:
    n = len(nums)
    if n == 1:
        return 1

    current_len = 1
    max_len = 1
    is_increasing = nums[1] > nums[0]

    for i in range(1, n):
        if is_increasing and nums[i] > nums[i - 1] or not is_increasing and nums[i] < nums[i - 1]:
            current_len += 1
        else:
            if current_len > max_len:
                max_len = current_len
            is_increasing = nums[i] > nums[i - 1]
            current_len = 1 if nums[i] == nums[i - 1] else 2

    return max(max_len, current_len)


print(longest_monotonic_subarray([1, 4, 3, 3, 2]))
print(longest_monotonic_subarray([3, 3, 3, 3]))
print(longest_monotonic_subarray([3, 2, 1]))
print(longest_monotonic_subarray([1]))
print(longest_monotonic_subarray([1, 1, 5]))
