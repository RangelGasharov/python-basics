def min_score_triangulation(values: list[int]) -> int:
    n = len(values)
    dp = [[0] * n for _ in range(n)]

    for length in range(2, n):
        for i in range(n - length):
            j = i + length
            dp[i][j] = min(values[i] * values[k] * values[j] + dp[i][k] + dp[k][j] for k in range(i + 1, j))
    return dp[0][n - 1]


print(min_score_triangulation([1, 2, 3]))
print(min_score_triangulation([3, 7, 4, 5]))
print(min_score_triangulation([1, 3, 1, 4, 1, 5]))
print(min_score_triangulation(
    [1, 2, 3, 4, 10, 10, 4, 10, 2, 9, 1, 4, 5, 11, 18, 19, 20, 9, 3, 5, 7, 1, 4, 8, 9, 2, 8, 5, 3, 4, 1, 15, 19, 1, 50,
     43, 21, 10, 25, 47, 39, 9, 10]))
