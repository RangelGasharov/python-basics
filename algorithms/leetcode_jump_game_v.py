def max_jumps(arr: list[int], d: int) -> int:
    n = len(arr)
    dp = [-1] * n

    def dfs(i):
        if dp[i] != -1:
            return dp[i]

        best = 1

        for nxt in range(i + 1, min(n, i + d + 1)):
            if arr[nxt] >= arr[i]:
                break

            best = max(best, 1 + dfs(nxt))

        for nxt in range(i - 1, max(-1, i - d - 1), -1):
            if arr[nxt] >= arr[i]:
                break

            best = max(best, 1 + dfs(nxt))

        dp[i] = best
        return dp[i]

    return max(dfs(i) for i in range(n))


print(max_jumps([6, 4, 14, 6, 8, 13, 9, 7, 10, 6, 12], 2))
print(max_jumps([3, 3, 3, 3, 3], 3))
print(max_jumps([7, 6, 5, 4, 3, 2, 1], 1))
