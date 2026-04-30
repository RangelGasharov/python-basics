from typing import List


def max_path_score(grid: List[List[int]], k: int) -> int:
    m = len(grid)
    n = len(grid[0])
    negative = -10 ** 9

    prev = [[negative] * (k + 1) for _ in range(n)]

    for i in range(m):
        curr = [[negative] * (k + 1) for _ in range(n)]

        for j in range(n):
            gain = grid[i][j]
            need = 1 if gain > 0 else 0

            limit = min(k, i + j)

            if i == 0 and j == 0:
                curr[0][0] = 0
                continue

            for c in range(need, limit + 1):
                best = negative

                if i > 0 and prev[j][c - need] != negative:
                    best = max(best, prev[j][c - need] + gain)

                if j > 0 and curr[j - 1][c - need] != negative:
                    best = max(best, curr[j - 1][c - need] + gain)

                curr[j][c] = best

        prev = curr

    result = max(prev[n - 1])
    return -1 if result < 0 else result


print(max_path_score([[0, 1], [2, 0]], 1))
print(max_path_score([[0, 1], [2, 0]], 2))
