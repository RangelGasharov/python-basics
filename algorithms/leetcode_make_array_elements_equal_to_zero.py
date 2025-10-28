def count_valid_selections(nums: list[int]) -> int:
    valid_selections = 0
    indices = []
    n = len(nums)
    sum_left = {0: nums[0]}
    sum_right = {n - 1: nums[n - 1]}

    for i in range(1, len(nums)):
        sum_left[i] = sum_left[i - 1] + nums[i]

    for i in range(n - 2, -1, -1):
        sum_right[i] = sum_right[(i + 1)] + nums[i]

    for i in range(len(nums)):
        if nums[i] == 0:
            indices.append(i)

    for index in indices:
        left_sum = sum_left.get(index - 1, 0)
        right_sum = sum_right.get(index + 1, 0)
        valid_selections += left_sum == right_sum or left_sum == right_sum + 1
        valid_selections += left_sum == right_sum or left_sum == right_sum - 1
    return valid_selections


print(count_valid_selections([1, 0, 2, 0, 3]))
print(count_valid_selections([2,3,4,0,4,1,0]))
