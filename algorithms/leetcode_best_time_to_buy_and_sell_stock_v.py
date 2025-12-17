def maximum_profit(prices: list[int], k: int) -> int:
    dp = [[float("-inf")] * 3 for _ in range(k + 1)]
    dp[0][0] = 0
    dp[0][1] = -prices[0]
    dp[0][2] = prices[0]

    for price in prices[1:]:
        new = [[float("-inf")] * 3 for _ in range(k + 1)]
        for t in range(k + 1):
            new[t][0] = dp[t][0]
            if t > 0:
                new[t][0] = max(
                    new[t][0],
                    dp[t - 1][1] + price,
                    dp[t - 1][2] - price
                )

            new[t][1] = max(dp[t][1], dp[t][0] - price)
            new[t][2] = max(dp[t][2], dp[t][0] + price)
        dp = new

    return max(dp[t][0] for t in range(k + 1))


print(maximum_profit([1, 7, 9, 8, 2], 2))
print(maximum_profit([12, 16, 19, 19, 8, 1, 19, 13, 9], 3))
