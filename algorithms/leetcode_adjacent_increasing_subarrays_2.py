def max_increasing_subarrays(nums):
    n = len(nums)
    if n < 2:
        return 0

    inc = [1] * n
    for i in range(1, n):
        if nums[i] > nums[i - 1]:
            inc[i] = inc[i - 1] + 1

    left = [1] * n
    for i in range(n - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            left[i] = left[i + 1] + 1

    max_k = 0
    for i in range(1, n):
        k = min(inc[i - 1], left[i])
        max_k = max(max_k, k)

    return max_k


print(max_increasing_subarrays([2, 5, 7, 8, 9, 2, 3, 4, 3, 1]))
print(max_increasing_subarrays([1, 2, 3, 4, 4, 4, 4, 5, 6, 7]))
print(max_increasing_subarrays([1, 2, 3, 4, 5, -5, -4, -3, -2, -1]))
