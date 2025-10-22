from bisect import bisect_left, bisect_right
from collections import Counter


def max_frequency(nums: list[int], k: int, num_operations: int) -> int:
    nums.sort()
    array_val_max_freq = max_frequency_of_array_val(nums, k, num_operations)

    left = 0
    other_val_max_freq = 0
    for right in range(len(nums)):
        while nums[right] > nums[left] + 2 * k:
            left += 1
        other_val_max_freq = max(other_val_max_freq, right - left + 1)
        if other_val_max_freq >= num_operations:
            other_val_max_freq = num_operations
            break

    return max(array_val_max_freq, other_val_max_freq)


def max_frequency_of_array_val(nums, k, num_operations):
    count = Counter(nums)

    max_freq = 0
    for val in count.keys():
        left = bisect_left(nums, val - k)
        right = bisect_right(nums, val + k) - 1
        freq = min(right - left + 1, num_operations + count[val])
        max_freq = max(max_freq, freq)

    return max_freq


print(max_frequency([1, 4, 5], 1, 2))
print(max_frequency([1, 4, 5], 1, 3))
print(max_frequency([5, 11, 20, 20], 5, 1))
