def count_covered_buildings(n: int, buildings: list[list[int]]) -> int:
    r_min = [n + 1] * (n + 1)
    r_max = [0] * (n + 1)

    c_min = [n + 1] * (n + 1)
    c_max = [0] * (n + 1)

    for x, y in buildings:
        r_min[y] = min(r_min[y], x)
        r_max[y] = max(r_max[y], x)

        c_min[x] = min(c_min[x], y)
        c_max[x] = max(c_max[x], y)

    result = 0

    for x, y in buildings:
        if r_min[y] < x < r_max[y] and c_min[x] < y < c_max[x]:
            result += 1

    return result


print(count_covered_buildings(3, [[0, 1], [1, 2], [2, 3], [3, 0]]))
print(count_covered_buildings(3, [[1, 2], [2, 2], [3, 2], [2, 1], [2, 3]]))
print(count_covered_buildings(3, [[1, 1], [1, 2], [2, 1], [2, 2]]))
print(count_covered_buildings(5, [[1, 3], [3, 2], [3, 3], [3, 5], [5, 3]]))
