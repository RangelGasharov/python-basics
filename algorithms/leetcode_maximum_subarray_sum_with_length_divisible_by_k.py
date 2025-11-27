def max_subarray_sum(nums: list[int], k: int) -> int:
    n = len(nums)
    prefix_sum = [0] * (n + 1)
    max_sum = float("-inf")
    min_prefix = [float("inf")] * k

    for i in range(n):
        prefix_sum[i+1] = prefix_sum[i] + nums[i]

    for j in range(n + 1):
        r = j % k

        if min_prefix[r] != float("inf"):
            max_sum = max(max_sum, prefix_sum[j] - min_prefix[r])

        min_prefix[r] = min(min_prefix[r], prefix_sum[j])

    return max_sum

print(max_subarray_sum([5, 4, 3, 2, 1], 3))
print(max_subarray_sum([-5, 1, 2, -3, 4], 2))
print(max_subarray_sum([1, 2], 1))
