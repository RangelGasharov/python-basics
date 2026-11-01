def min_moves(self, nums: list[int]) -> int:
    return sum(nums) - len(nums) * min(nums)