def min_operations(nums: list[int], k: int) -> int:
    nums_sum = sum(nums)
    return nums_sum % k
