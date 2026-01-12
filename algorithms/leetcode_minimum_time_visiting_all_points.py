def min_time_to_visit_all_points(points: list[list[int]]) -> int:
    total_time = 0
    for i in range(1, len(points)):
        x_distance = abs(points[i - 1][0] - points[i][0])
        y_distance = abs(points[i - 1][1] - points[i][1])
        total_time += max(x_distance, y_distance)
    return total_time


print(min_time_to_visit_all_points([[1, 1], [6, -2]]))
print(min_time_to_visit_all_points([[1, 1], [3, 4], [-1, 0]]))
print(min_time_to_visit_all_points([[3, 2], [-2, 2]]))
