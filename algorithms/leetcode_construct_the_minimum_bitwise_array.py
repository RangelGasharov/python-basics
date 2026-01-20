def min_bitwise_array(nums: list[int]) -> list[int]:
    result = [-1] * len(nums)
    for i, num in enumerate(nums):
        if num % 2:
            result[i] = (num - ((num + 1) & (-num - 1)) // 2)
    return result


print(min_bitwise_array([1, 2, 3, 4, 5, 6, 7]))
print(min_bitwise_array([2, 3, 5, 7]))
print(min_bitwise_array([11, 13, 31]))
