def uniform_array(nums1: list[int]) -> bool:
    min_num = min(nums1)

    if min_num & 1:
        return True

    for num in nums1:
        if num & 1:
            return False

    return True


print(uniform_array([1, 4, 7]))
print(uniform_array([2, 3]))
print(uniform_array([4, 6]))
