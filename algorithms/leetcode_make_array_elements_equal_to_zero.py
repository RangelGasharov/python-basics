from itertools import groupby


def countValidSelections(nums: list[int]) -> int:
    valid_selections = 0
    indices = []

    for i in range(len(nums)):
        if nums[i] == 0:
            indices.append(i)

    def is_valid(numbers: list, position: int, initial_direction: int):
        nums = list(numbers)
        current_direction = initial_direction
        i = position + current_direction
        while 0 <= i < len(numbers):
            if nums[i] > 0:
                current_direction = -current_direction
                nums[i] -= 1
                i += current_direction
            else:
                i += current_direction
        g = groupby(nums)
        return next(g, True) and not next(g, False)

    for index in indices:
        valid_selections += 1 * (is_valid(nums, index, -1))
        valid_selections += 1 * (is_valid(nums, index, 1))
    return valid_selections


print(countValidSelections([1, 0, 2, 0, 3]))
