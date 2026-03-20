from typing import List


def min_abs_diff(grid: List[List[int]], k: int) -> List[List[int]]:
    rows = len(grid)
    cols = len(grid[0])

    result = [[0] * (cols - k + 1) for _ in range(rows - k + 1)]

    for i in range(rows - k + 1):
        for j in range(cols - k + 1):
            v = sorted(set(
                grid[x][y]
                for x in range(i, i + k)
                for y in range(j, j + k)
            ))
            if len(v) <= 1:
                result[i][j] = 0
            else:
                result[i][j] = min(v[p + 1] - v[p] for p in range(len(v) - 1))

    return result


print(min_abs_diff([[1]], 1))
print(min_abs_diff([[1, 8], [3, -2]], 2))
print(min_abs_diff([[3, -1]], 1))
print(min_abs_diff([[1, -2, 3, 4], [2, 3, 5, 4], [2, 3, 5, 4]], 2))
