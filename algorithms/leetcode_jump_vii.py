def canReach(s: str, min_jump: int, max_jump: int) -> bool:
    n = len(s)

    if int(s[-1]): return False

    dp = [False] * n
    dp[0] = True
    reach, maxR = 0, max_jump

    for i in range(min_jump, n):
        if i > maxR:
            return False

        reach += dp[i - min_jump]

        if i > max_jump:
            reach -= dp[i - max_jump - 1]

        if reach and not int(s[i]):
            dp[i] = True
            maxR = i + max_jump

    return reach > 0


print(canReach("011010", 2, 3))
print(canReach("01101110", 2, 3))
