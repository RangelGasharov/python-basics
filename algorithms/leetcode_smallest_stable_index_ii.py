def first_stable_index(nums: list[int], k: int) -> int:
    n = len(nums)
    min_num = float("inf")
    min_at_index = [float("inf")] * n
    max_num = -min_num

    for i in range(n - 1, -1, -1):
        if nums[i] < min_num:
            min_num = nums[i]

        min_at_index[i] = min_num

    for i in range(n):
        if nums[i] > max_num:
            max_num = nums[i]
        if max_num - min_at_index[i] <= k:
            return i
    return -1

print(first_stable_index([5, 0, 1, 4], 3))
print(first_stable_index([3, 2, 1], 1))
print(first_stable_index([0], 0))