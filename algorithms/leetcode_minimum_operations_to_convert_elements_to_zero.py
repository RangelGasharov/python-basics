def min_operations(nums: list[int]) -> int:
    stack = []
    result = 0
    for num in nums:
        while stack and stack[-1] > num:
            stack.pop()
        if num == 0:
            continue
        if not stack or stack[-1] < num:
            result += 1
            stack.append(num)
    return result


print(min_operations([0, 2]))
print(min_operations([3, 1, 2, 1]))
print(min_operations([1, 2, 1, 2, 1, 2]))
print(min_operations(
    [1, 3, 2, 4, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19, 0, 1000, 2000, 3000, 4000, 5000, 6000, 7000,
     8000, 9000, 10000, 0, 1234, 2345, 3456, 4567, 5678, 6789, 7890, 8901, 9012, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10,
     20, 30, 40, 50, 60, 70, 80, 90, 0, 12345, 23456, 34567, 45678, 56789, 67890, 78901, 89012, 90123, 100000]))
