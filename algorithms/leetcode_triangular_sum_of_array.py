def triangular_sum(nums: list[int]) -> int:
    while len(nums) > 1:
        for i in range(len(nums) - 1):
            nums[i] = (nums[i] + nums[i + 1]) % 10
        nums.pop()
    return nums[0]


print(triangular_sum([1, 2, 3, 4, 5]))
print(triangular_sum([5]))
print(triangular_sum(
    [1, 2, 3, 4, 5, 9, 1, 2, 6, 3, 1, 8, 3, 9, 1, 5, 2, 3, 4, 8, 6, 5, 5, 5, 9, 0, 1, 0, 2, 3, 6, 2, 1, 7, 9, 8, 3, 2,
     2, 4, 5, 6, 7, 8, 9, 1, 3, 7, 2, 5, 8, 3, 5, 1, 2, 0, 2, 3, 6, 4, 2, 1, 7, 0]))
