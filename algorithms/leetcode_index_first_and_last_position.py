def search_range(nums, target):
    if len(nums) == 0:
        return [-1, -1]

    def find_left():
        left, right = 0, len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        if left < len(nums) and nums[left] == target:
            return left
        return -1

    def find_right():
        left, right = 0, len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] <= target:
                left = middle + 1
            else:
                right = middle - 1
        if right >= 0 and nums[right] == target:
            return right
        return -1

    return [find_left(), find_right()]


print(search_range([5, 7, 7, 8, 8, 10], 8))
print(search_range([5, 7, 7, 8, 8, 10], 6))
print(search_range([], 0))
print(search_range([7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9], 8))
print(search_range(
    [-999985131, -999953607, -999953607, -999915742, -999883817, -999849817, -999822901, -999815377, -999810801, -68594,
     -49967, 20394, 114012, 999969829, 999973689, 999975494], -999953607))
