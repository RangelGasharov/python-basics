from typing import List


def maximumScore(self, grid: List[List[int]]) -> int:
    n = len(grid)
    m = len(grid[0])
    if m == 1:
        return 0

    col = [[0] * (n + 1) for _ in range(m)]
    for j in range(m):
        for i in range(n):
            col[j][i + 1] = col[j][i] + grid[i][j]

    dp = [[0] * (n + 1) for _ in range(n + 1)]
    pref_max = [[0] * (n + 1) for _ in range(n + 1)]
    suff_max = [[0] * (n + 1) for _ in range(n + 1)]

    for c in range(1, m):

        new_dp = [[0] * (n + 1) for _ in range(n + 1)]

        for curr in range(n + 1):
            for prev in range(n + 1):

                if curr <= prev:
                    gain = col[c][prev] - col[c][curr]

                    new_dp[curr][prev] = max(
                        new_dp[curr][prev],
                        suff_max[prev][0] + gain
                    )
                else:
                    gain = col[c - 1][curr] - col[c - 1][prev]

                    new_dp[curr][prev] = max(
                        new_dp[curr][prev],
                        suff_max[prev][curr],
                        pref_max[prev][curr] + gain
                    )

        for curr in range(n + 1):

            pref_max[curr][0] = new_dp[curr][0]

            for prev in range(1, n + 1):
                penalty = 0
                if prev > curr:
                    penalty = col[c][prev] - col[c][curr]

                pref_max[curr][prev] = max(
                    pref_max[curr][prev - 1],
                    new_dp[curr][prev] - penalty
                )

            suff_max[curr][n] = new_dp[curr][n]

            for prev in range(n - 1, -1, -1):
                suff_max[curr][prev] = max(
                    suff_max[curr][prev + 1],
                    new_dp[curr][prev]
                )

        dp = new_dp

    result = 0
    for k in range(n + 1):
        result = max(result, dp[0][k], dp[n][k])

    return result