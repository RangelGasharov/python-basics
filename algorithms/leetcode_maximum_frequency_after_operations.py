def max_frequency(nums: list[int], k: int, num_operations: int) -> int:
    max_value = max(nums) + k + 2
    count = [0] * max_value

    for num in nums:
        count[num] += 1

    for i in range(1, max_value):
        count[i] += count[i - 1]

    res = 0
    for i in range(max_value):
        left = max(0, i - k)
        right = min(max_value - 1, i + k)
        total = count[right] - (count[left - 1] if left else 0)
        freq = count[i] - (count[i - 1] if i else 0)
        res = max(res, freq + min(num_operations, total - freq))

    return res


print(max_frequency([1, 4, 5], 1, 2))
print(max_frequency([1, 4, 5], 1, 3))
print(max_frequency([5, 11, 20, 20], 5, 1))
