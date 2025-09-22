def max_frequency_elements(nums: list[int]) -> int:
    if len(nums) == 0:
        return 0
    num_frequency = {}
    for num in nums:
        if num not in num_frequency:
            num_frequency[num] = 1
        else:
            num_frequency[num] += 1
    highest_frequency = 0
    num_of_max = 0

    for key, val in num_frequency.items():
        if val > highest_frequency:
            num_of_max = 1
            highest_frequency = val
        elif val == highest_frequency:
            num_of_max += 1
    return num_of_max * highest_frequency


print(max_frequency_elements([1, 2, 5, 2, 1]))
print(max_frequency_elements([1, 1, 1]))
print(max_frequency_elements([1, 2, 3, 4, 5]))
