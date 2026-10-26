from typing import List


def count_islands(self, grid: List[List[int]], k: int) -> int:
    m, n = len(grid), len(grid[0])
    result = 0

    def dfs(i: int, j: int) -> int:
        if grid[i][j] == 0 or i < 0 or i >= m or j < 0 or j >= n:
            return 0

        s = grid[i][j]
        grid[i][j] = 0

        s += dfs(i + 1, j)
        s += dfs(i - 1, j)
        s += dfs(i, j + 1)
        s += dfs(i, j - 1)
        return s

    for i in range(m):
        for j in range(n):
            if grid[i][j] > 0:
                if dfs(i, j) % k == 0:
                    result += 1
    return result


print(count_islands([[0, 2, 1, 0, 0], [0, 5, 0, 0, 5], [0, 0, 1, 0, 0], [0, 1, 4, 7, 0], [0, 2, 0, 0, 8]]))
print(count_islands([[3, 0, 3, 0], [0, 3, 0, 3], [3, 0, 3, 0]]))
