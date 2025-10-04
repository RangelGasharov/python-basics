def max_area(height: list[int]) -> int:
    left = 0
    right = len(height) - 1
    largest_area = 0
    while left < right:
        area = min(height[left], height[right]) * (right - left)
        largest_area = max(largest_area, area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return largest_area


print(max_area([1, 1]))
print(max_area([7, 1, 7]))
print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))
