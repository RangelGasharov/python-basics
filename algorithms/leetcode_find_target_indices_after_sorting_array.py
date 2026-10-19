def target_indices(nums: list[int], target: int) -> list[int]:
    less_than = 0
    num_of_target = 0

    for num in nums:
        if num == target:
            num_of_target += 1
        elif num < target:
            less_than += 1

    return list(range(less_than, less_than + num_of_target))


print(target_indices([1, 2, 5, 2, 3], 2))
print(target_indices([1, 2, 5, 2, 3], 3))
print(target_indices([1, 2, 5, 2, 3], 5))
print(target_indices([1, 2, 5, 2, 3], 6))
