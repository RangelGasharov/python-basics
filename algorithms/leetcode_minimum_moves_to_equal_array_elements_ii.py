def min_moves2(nums: list[int]) -> int:
    nums.sort()
    change = nums[len(nums) // 2]
    return sum(abs(change - num) for num in nums)


print(min_moves2([1, 2, 3]))
print(min_moves2([1, 10, 2, 9]))
