def champagne_tower(poured: int, query_row: int, query_glass: int) -> float:
    dp = [poured]
    for i in range(query_row):
        next_row = [0.0] * (len(dp) + 1)
        for j in range(i + 1):
            overflow = (dp[j] - 1.0) / 2.0
            if overflow > 0:
                next_row[j] += overflow
                next_row[j + 1] += overflow
        dp = next_row
    return min(1.0, dp[query_glass])


print(champagne_tower(10, 2, 2))
print(champagne_tower(10, 5, 3))
print(champagne_tower(100000, 100, 48))
