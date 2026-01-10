def minimum_delete_sum(s1: str, s2: str) -> int:
    n = len(s1)
    m = len(s2)
    s1_list = list(s1)
    s2_list = list(s2)

    dp = [[float("inf") for _ in range(m + 1)] for _ in range(n + 1)]
    dp[0][0] = 0

    for i in range(1, n + 1):
        dp[i][0] = ord(s1_list[i - 1]) + dp[i - 1][0]

    for j in range(1, m + 1):
        dp[0][j] = ord(s2_list[j - 1]) + dp[0][j - 1]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1_list[i - 1] == s2_list[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(ord(s2_list[j - 1]) + dp[i][j - 1], ord(s1_list[i - 1]) + dp[i - 1][j])
    return dp[n][m]


print(minimum_delete_sum("sea", "eat"))
print(minimum_delete_sum("delete", "leet"))
