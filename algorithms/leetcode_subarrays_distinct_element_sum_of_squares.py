def sum_counts(nums: List[int]) -> int:
    total = 0
    n = len(nums)
    for i in range(n):
        seen = set()
        for j in range(i, n):
            seen.add(nums[j])
            total += len(seen) ** 2
    return total


print(sum_counts([1, 2, 1]))
print(sum_counts([11]))
