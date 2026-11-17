from algorithms.edabit_adding_numbers import add


def minimum_changes(s: str, k: int) -> int:
    n = len(s)
    INF = float("inf")

    mism = [None] * n
    for g in range(1, n):
        pref = [0]
        for a, b in zip(s, s[g:]):
            pref.append(pref[-1] + (a != b))
        mism[g] = pref

    cost = [[INF] * (n + 1) for _ in range(n + 1)]

    for d in range(1, n // 2 + 1):
        two_back = [0] * (n + 1)
        one_back = [0] * (n + 1)
        for m in range(2, n // d + 1):
            L = m * d
            pref = mism[L - d]
            cur = [two_back[i + d] + pref[i + d] - pref[i]
                   for i in range(n - L + 1)]
            for i, c in enumerate(cur):
                if c < cost[i + L][i]:
                    cost[i + L][i] = c
            two_back, one_back = one_back, cur

    dp = [0] + [INF] * n
    for p in range(1, k + 1):
        new = [INF] * (n + 1)
        lo = 2 * (p - 1)
        for j in range(2 * p, n - 2 * (k - p) + 1):
            new[j] = min(map(add, dp[lo:j - 1], cost[j][lo:j - 1]))
        dp = new
    return dp[n]


print(minimum_changes("abcac", 2))
