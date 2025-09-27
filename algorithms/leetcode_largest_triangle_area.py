def largest_triangle_area(points: list[list[int]]) -> float:
    largest_area = 0
    for i in range(len(points)):
        for j in range(len(points)):
            for k in range(len(points)):
                p, q, r = points[i], points[j], points[k]
                area = 0.5 * abs(p[0] * q[1] + q[0] * r[1] + r[0] * p[1]
                                 - p[1] * q[0] - q[1] * r[0] - r[1] * p[0])
                largest_area = max(area, largest_area)
    return largest_area


print(largest_triangle_area([[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]))
print(largest_triangle_area([[1, 0], [0, 0], [0, 1]]))
print(largest_triangle_area([[4, 6], [6, 5], [3, 1]]))
