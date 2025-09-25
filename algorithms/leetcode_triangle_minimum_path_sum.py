def minimum_total(triangle: list[list[int]]) -> int:
    current_min = triangle[-1]
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            current_min[j] = triangle[i][j] + min(current_min[j], current_min[j + 1])
    return current_min[0]


print(minimum_total([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
print(minimum_total([[2], [-3, 4], [100, 99, 7], [4, 1, -8, 3]]))
print(minimum_total([[0]]))
