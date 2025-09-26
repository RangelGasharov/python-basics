def triangle_number(nums: list[int]) -> int:
    nums.sort()
    amount_valid_triangles = 0

    for k in range(len(nums) - 1, 1, -1):
        i, j = 0, k - 1
        while i < j:
            if nums[i] + nums[j] > nums[k]:
                amount_valid_triangles += (j - i)
                j -= 1
            else:
                i += 1

    return amount_valid_triangles


print(triangle_number([2, 2, 3, 4]))
print(triangle_number([4, 2, 3, 4]))
print(triangle_number([1, 2, 2, 3]))
