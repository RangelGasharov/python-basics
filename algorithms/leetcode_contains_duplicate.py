def contains_duplicate(nums):
    return len(nums) != len(set(nums))


print(contains_duplicate([1, 2, 3, 4, 5, 6, 7, 8]))
print(contains_duplicate([1, 100, 100, 300, 2]))
print(contains_duplicate([84, 9, 37, 25, 100]))
