def max_building(n: int, restrictions: list[list[int]]) -> int:
    restrictions.append([1, 0])
    restrictions.sort()
    len_rest = len(restrictions)

    def y_cap(x1, y1, x2, y2):
        return min(y2, y1 + abs(x2 - x1))

    def y_peak(x1, y1, x2, y2):
        return (y1 + y2 + x2 - x1) >> 1

    for i in range(1, len_rest):
        restrictions[i][1] = y_cap(*restrictions[i - 1], *restrictions[i])

    for i in range(len_rest - 2, -1, -1):
        restrictions[i][1] = y_cap(*restrictions[i + 1], *restrictions[i])

    res = 0
    for i in range(1, len_rest):
        res = max(res, y_peak(*restrictions[i - 1], *restrictions[i]))

    return max(res, restrictions[-1][1] + n - restrictions[-1][0])


print(max_building(5, [[2, 1], [4, 1]]))
print(max_building(6, []))
print(max_building(10, [[5, 3], [2, 5], [7, 4], [10, 3]]))
