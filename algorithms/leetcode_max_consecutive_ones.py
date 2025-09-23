def longest_ones(nums: list[int], k: int):
    max_number = 0
    num_zeros = 0

    left = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            num_zeros += 1

        while num_zeros > k:
            if nums[left] == 0:
                num_zeros -= 1
            left += 1
        max_number = max(max_number, (right - left + 1))
    return max_number


print(longest_ones([0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1], 3))
print(longest_ones([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3))
print(longest_ones([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))
