def largest_square_area(bottom_left: list[list[int]], top_right: list[list[int]]) -> int:
    max_length = 0
    n = len(bottom_left)

    for i in range(n):
        for j in range(i + 1, n):
            min_x = max(bottom_left[i][0], bottom_left[j][0])
            max_x = min(top_right[i][0], top_right[j][0])

            min_y = max(bottom_left[i][1], bottom_left[j][1])
            max_y = min(top_right[i][1], top_right[j][1])

            width = max_x - min_x
            height = max_y - min_y

            if width > 0 and height > 0:
                length = min(width, height)
                max_length = max(max_length, length)

    return max_length * max_length


print(largest_square_area([[1, 1], [3, 3], [3, 1]], [[2, 2], [4, 4], [4, 2]]))
print(largest_square_area([[1, 1], [2, 2], [1, 2]], [[3, 3], [4, 4], [3, 4]]))
print(largest_square_area([[1, 1], [1, 3], [1, 5]], [[5, 5], [5, 7], [5, 9]]))
print(largest_square_area([[1, 1], [2, 2], [3, 1]], [[3, 3], [4, 4], [6, 6]]))
