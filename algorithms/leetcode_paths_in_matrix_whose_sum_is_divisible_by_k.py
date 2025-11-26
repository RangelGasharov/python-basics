def number_of_paths(grid: list[list[int]], k: int) -> int:
    MOD = 10 ** 9 + 7
    m, n = len(grid), len(grid[0])

    dp = [[[0] * k for _ in range(n)] for __ in range(m)]

    dp[0][0][grid[0][0] % k] = 1

    for r in range(m):
        for c in range(n):
            val_mod = grid[r][c] % k

            if r > 0:
                for mod in range(k):
                    new_mod = (mod + val_mod) % k
                    dp[r][c][new_mod] = (dp[r][c][new_mod] + dp[r - 1][c][mod]) % MOD

            if c > 0:
                for mod in range(k):
                    new_mod = (mod + val_mod) % k
                    dp[r][c][new_mod] = (dp[r][c][new_mod] + dp[r][c - 1][mod]) % MOD

    return dp[m - 1][n - 1][0]


print(number_of_paths([[5, 2, 4], [3, 0, 5], [0, 7, 2]], 3))
print(number_of_paths([[0, 0]], 5))
print(number_of_paths([[7, 3, 4, 9], [2, 3, 6, 2], [2, 3, 7, 0]], 1))
