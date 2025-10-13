def product_except_self(nums: list[int]) -> list[int]:
    n = len(nums)
    mult_left = [None] * n
    mult_left[0] = nums[0]
    mult_right = [None] * n
    mult_right[-1] = nums[-1]
    for i in range(1, n):
        mult_left[i] = mult_left[i - 1] * nums[i]
    for i in range(n - 2, -1, -1):
        mult_right[i] = mult_right[i + 1] * nums[i]
    result = [mult_right[1]]
    for i in range(1, n - 1):
        result.append(mult_left[i - 1] * mult_right[i + 1])
    result.append(mult_left[-2])
    return result


print(product_except_self([1, 2, 3, 4, 5]))
print(product_except_self([4, 3, 2, 1, 2]))
