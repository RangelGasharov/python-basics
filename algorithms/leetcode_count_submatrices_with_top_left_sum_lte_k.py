from typing import List


def countSubmatrices(grid: List[List[int]], k: int) -> int:
    rows = len(grid)
    cols = len(grid[0])

    prev_row_sums = [0] * (cols + 1)
    result = 0

    for r in range(rows):
        current_row_prefix = 0
        for c in range(cols):
            current_row_prefix += grid[r][c]
            prev_row_sums[c + 1] += current_row_prefix

            if prev_row_sums[c + 1] <= k:
                result += 1
    return result


print(countSubmatrices([[7, 6, 3], [6, 6, 1]], 18))
print(countSubmatrices([[7, 2, 9], [1, 5, 0], [2, 6, 6]], 20))
