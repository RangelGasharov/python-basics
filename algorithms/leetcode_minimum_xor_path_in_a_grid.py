def min_cost(grid: list[list[int]]) -> int:
    dp = [set()] * len(grid[0])
    dp[0] = {0}

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            previous = dp[j].union(dp[j - 1]) if j else dp[j]
            dp[j] = set(x ^ grid[i][j] for x in previous)

    return min(dp[-1])


print(min_cost([[1, 2], [3, 4]]))
print(min_cost([[6, 7], [5, 8]]))
print(min_cost([[2, 7, 5]]))
