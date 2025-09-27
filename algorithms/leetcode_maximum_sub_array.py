def max_sub_array(nums: list[int]) -> int:
    current_sum = 0
    maximum_sum = nums[0]
    for num in nums:
        current_sum += num
        if current_sum > maximum_sum:
            maximum_sum = current_sum
        if current_sum < 0:
            current_sum = 0
    return maximum_sum


print(max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(max_sub_array([1]))
print(max_sub_array([5, 4, -1, 7, 8]))
print(max_sub_array([-2, 5, -10, 19]))
print(max_sub_array([-1]))
