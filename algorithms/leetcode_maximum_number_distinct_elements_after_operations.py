def max_distinct_elements(nums: list[int], k: int) -> int:
    n = len(nums)
    if n <= (k * 2) + 1:
        return n
    nums.sort()
    result = 0
    current = float("-inf")

    for num in nums:
        target = max(current + 1, num - k)

        if target <= num + k:
            current = target
            result += 1
        else:
            current = max(current, num)
    return result


print(max_distinct_elements([1, 2, 2, 3, 3, 4], 2))
print(max_distinct_elements([4, 4, 4, 4], 1))
print(max_distinct_elements([1, 1, 1, 1, 1, 1, 1, 1, 5, 5, 5], 3))
