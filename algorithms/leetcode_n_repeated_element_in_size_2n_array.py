def repeated_n_times(nums: list[int]) -> int:
    for distance in range(1, 4):
        for i in range(len(nums) - distance):
            if nums[i] == nums[i + distance]:
                return nums[i]
    return -1


print(repeated_n_times([5, 1, 5, 2, 5, 3, 5, 4]))
print(repeated_n_times([1, 6, 6, 9]))
print(repeated_n_times([6, 1, 6, 9]))
print(repeated_n_times([2, 1, 2, 5, 3, 2]))
