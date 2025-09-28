def summary_ranges(nums: list[int]) -> list[str]:
    if len(nums) == 0:
        return []
    result = []
    lower_bound = nums[0]
    upper_bound = nums[0]

    for i in range(1, len(nums)):
        a = nums[i - 1]
        b = nums[i]

        if a == b - 1:
            upper_bound = b
        else:
            if lower_bound == upper_bound:
                result.append(str(lower_bound))
            else:
                result.append(f"{lower_bound}->{upper_bound}")
            lower_bound = b
            upper_bound = b
    if lower_bound == upper_bound:
        result.append(str(lower_bound))
    else:
        result.append(f"{lower_bound}->{upper_bound}")

    return result


print(summary_ranges([0, 1, 2, 4, 5, 7]))
print(summary_ranges([0, 2, 3, 4, 6, 8, 9]))
print(summary_ranges([0, 2, 4, 6, 8, 9]))
print(summary_ranges([]))
print(summary_ranges([1]))
