def largest_perimeter(nums: list[int]) -> int:
    nums.sort(reverse=True)
    i, j, k = 0, 1, 2

    while not (nums[i] < nums[j] + nums[k]):
        j += 1
        k += 1
        if k == len(nums):
            return 0
    current_max = nums[i] + nums[j] + nums[k]
    return current_max


print(largest_perimeter([2, 1, 2]))
print(largest_perimeter([1, 2, 1, 10]))
print(largest_perimeter([10, 4, 5, 7, 3]))
