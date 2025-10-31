def get_sneaky_numbers(nums: list[int]) -> list[int]:
    count = {}
    result = []
    for i in range(len(nums)):
        if nums[i] not in count:
            count[nums[i]] = 1
        else:
            result.append(nums[i])
    return result


print(get_sneaky_numbers([0, 1, 1, 0]))
print(get_sneaky_numbers([0, 3, 2, 1, 3, 2]))
print(get_sneaky_numbers([7, 1, 5, 4, 3, 4, 6, 0, 9, 5, 8, 2]))
