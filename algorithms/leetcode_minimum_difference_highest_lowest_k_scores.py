def minimum_difference(nums: list[int], k: int) -> int:
    nums.sort()
    n = len(nums)
    if n <= 1:
        return 0
    lowest = float("inf")
    for i in range(n - k + 1):
        lowest = min(lowest, nums[i + k - 1] - nums[i])
    return lowest


print(minimum_difference([90], 1))
print(minimum_difference([9, 4, 1, 7], 2))
print(minimum_difference(
    [134, 15, 13, 6, 52, 15, 1, 616, 1, 51, 51, 43, 324, 613, 2, 63, 614, 46, 361, 3, 616, 43, 63, 51, 77, 135, 13, 6,
     23, 467, 2, 3], 5))
