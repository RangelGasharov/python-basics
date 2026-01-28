from collections import defaultdict
from typing import List


def min_cost(grid: List[List[int]], k: int) -> int:
    n = len(grid[0])
    m = len(grid)

    dictionary = defaultdict(list)
    for i in range(m):
        for j in range(n):
            dictionary[grid[i][j]].append((i, j))

    inf = float("inf")

    dp = [[inf] * n for _ in range(m)]
    dp[0][0] = 0

    def update():
        for i in range(m):
            for j in range(n):
                temp = grid[i][j] + min(dp[i - 1][j] if i else inf, dp[i][j - 1] if j else inf)
                if temp < dp[i][j]:
                    dp[i][j] = temp

    update()

    keys = sorted(dictionary, reverse=True)
    for _ in range(k):
        dist = inf
        for key in keys:
            for i, j in dictionary[key]:
                if dp[i][j] < dist: dist = dp[i][j]
            for i, j in dictionary[key]:
                dp[i][j] = dist
        update()
    return dp[-1][-1]


print(min_cost([[1, 3, 3], [2, 5, 4], [4, 3, 5]], 2))
print(min_cost([[1, 3, 3], [2, 5, 4], [4, 3, 5]], 3))
print(min_cost([[1, 2], [2, 3], [3, 4]], 1))
