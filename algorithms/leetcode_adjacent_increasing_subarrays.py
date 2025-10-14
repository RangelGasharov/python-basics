def has_increasing_subarrays(nums: list[int], k: int) -> bool:
    n = len(nums)
    if k == 1:
        return n >= 2
    if n < 2 * k:
        return False
    inc_len = 1
    is_inc_subarray = [False] * n

    for i in range(1, n):
        if nums[i] > nums[i - 1]:
            inc_len += 1
        else:
            inc_len = 1

        if inc_len >= k:
            is_inc_subarray[i] = True

    for i in range(k - 1, n - k):
        if is_inc_subarray[i] and is_inc_subarray[i + k]:
            return True

    return False


print(has_increasing_subarrays([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
print(has_increasing_subarrays([-15, 19], 1))
print(has_increasing_subarrays([6, 13, -17, -20, 2], 2))
