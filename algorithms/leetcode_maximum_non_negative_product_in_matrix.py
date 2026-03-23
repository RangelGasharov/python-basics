from typing import List


def max_product_path(grid: List[List[int]]) -> int:
    row = len(grid)
    col = len(grid[0])

    dp = [[[0, 0] for _ in range(col)] for _ in range(row)]
    dp[0][0] = [grid[0][0], grid[0][0]]

    for r in range(1, row):
        val = dp[r - 1][0][0] * grid[r][0]
        dp[r][0] = [val, val]

    for c in range(1, col):
        val = dp[0][c - 1][0] * grid[0][c]
        dp[0][c] = [val, val]

    for r in range(1, row):
        for c in range(1, col):
            options = [
                dp[r - 1][c][0] * grid[r][c],
                dp[r - 1][c][1] * grid[r][c],
                dp[r][c - 1][0] * grid[r][c],
                dp[r][c - 1][1] * grid[r][c],
            ]
            dp[r][c] = [max(options), min(options)]

    if dp[row - 1][col - 1][0] < 0:
        return -1

    return dp[row - 1][col - 1][0] % (10 ** 9 + 7)


print(max_product_path([[-1, -2, -3], [-2, -3, -3], [-3, -3, -2]]))
print(max_product_path([[1, -2, 1], [1, -2, 1], [3, -4, 1]]))
print(max_product_path([[1, 3], [0, -4]]))
print(max_product_path([[-3, -3, -2, -2, -1, -3, -4, -4, -4, -2, -2, -2, -3, -1, 0],
                        [-3, -2, -1, -2, -3, -1, -1, -1, -2, -2, -1, -1, -2, -4, -3],
                        [-2, -3, -4, -3, -3, -1, -4, -4, -2, -2, -2, -1, -4, -1, -2],
                        [-2, -4, -3, -4, -3, -4, -2, -1, -3, -1, -2, -4, -2, -1, -3]]))
