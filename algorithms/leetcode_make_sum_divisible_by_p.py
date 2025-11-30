def min_subarray(nums: list[int], p: int) -> int:
    total = sum(nums)
    target = total % p
    if target == 0:
        return 0

    prefix_sum = 0
    mod_index = {0: -1}
    min_length = len(nums)

    for i, num in enumerate(nums):
        prefix_sum = (prefix_sum + num) % p
        needed = (prefix_sum - target + p) % p
        if needed in mod_index:
            min_length = min(min_length, i - mod_index[needed])
        mod_index[prefix_sum] = i

    return min_length if min_length < len(nums) else -1


print(min_subarray([3, 1, 4, 2], 6))
print(min_subarray([6, 3, 5, 2], 9))
print(min_subarray([1, 2, 3], 3))
