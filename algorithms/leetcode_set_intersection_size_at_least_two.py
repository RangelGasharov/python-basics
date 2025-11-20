def intersection_size_two(intervals: list[list[int]]) -> int:
    result = 0
    current = []

    intervals.sort(key=lambda x: x[1])

    for start, end in intervals:
        if not current or start > current[1]:
            result += 2
            current = [end - 1, end]
        elif start > current[0]:
            result += 1
            if current[1] == end:
                current = [end - 1, end]
            else:
                current = [current[1], end]
    return result


print(intersection_size_two([[1, 2], [3, 4]]))
print(intersection_size_two([[1, 3], [3, 7], [8, 9]]))
print(intersection_size_two([[1, 3], [1, 4], [2, 5], [3, 5]]))
print(intersection_size_two([[1, 2], [2, 3], [2, 4], [4, 5]]))
