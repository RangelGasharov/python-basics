def check_overlap(radius: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int) -> bool:
    x = max(x1, min(x_center, x2)) - x_center
    y = max(y1, min(y_center, y2)) - y_center

    return x * x + y * y <= radius * radius


print(check_overlap(1, 0, 0, 1, -1, 3, 1))
print(check_overlap(1, 1, 1, 1, -3, 2, -1))
print(check_overlap(1, 0, 0, -1, 0, 0, 1))
