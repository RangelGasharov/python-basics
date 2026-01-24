def min_pair_sum(nums: list[int]) -> int:
    nums.sort()
    i = 0
    j = len(nums) - 1
    result = 0

    while i < j:
        current_sum = nums[i] + nums[j]
        result = max(result, current_sum)
        i += 1
        j -= 1
    return result



print(min_pair_sum([1, 2, 3, 4]))
print(min_pair_sum([3, 5, 2, 3]))
print(min_pair_sum([3, 5, 4, 2, 4, 6]))