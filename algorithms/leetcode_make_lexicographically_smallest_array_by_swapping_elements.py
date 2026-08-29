def lexicographically_smallest_array(nums: list[int], limit: int) -> list[int]:
    groups = []
    gmap = {}

    for value in sorted(nums):
        if not groups or value - groups[-1][-1] > limit:
            groups.append([])
        groups[-1].append(value)
        gmap[value] = len(groups) - 1

    itr = [iter(g) for g in groups]

    for i in range(len(nums)):
        nums[i] = next(itr[gmap[nums[i]]])

    return nums


print(lexicographically_smallest_array([1, 5, 3, 9, 8], 2))
print(lexicographically_smallest_array([1, 7, 6, 18, 2, 1], 3))
print(lexicographically_smallest_array([1, 7, 28, 19, 10], 3))
