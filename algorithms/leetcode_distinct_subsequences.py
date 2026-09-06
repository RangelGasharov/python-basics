def num_distinct(s: str, t: str) -> int:
    m = len(s)
    n = len(t)

    if m < n:
        return 0

    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][n] = 1

    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if s[i] == t[j]:
                dp[i][j] = dp[i + 1][j + 1] + dp[i + 1][j]
            else:
                dp[i][j] = dp[i + 1][j]

    return dp[0][0]


print(num_distinct("rabbbit", "rabbbit"))
print(num_distinct("babgbag", "bag"))
