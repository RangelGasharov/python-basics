def minimum_operations(nums: list[int]) -> int:
    result = 0
    for i in range(len(nums)):
        result += min(nums[i] % 3, 3 - (nums[i] % 3))
    return result


print(minimum_operations([1, 2, 3, 4]))
print(minimum_operations([3,6,9]))
print(minimum_operations([1,10,20,4,7,27,4,3]))
