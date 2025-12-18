def max_profit(prices: list[int], strategy: list[int], k: int) -> int:
    sp = [s * p for s, p in zip(strategy, prices)]
    n = len(prices)

    base_sum = sum(sp)
    h = k // 2
    old = sum(sp[:k])
    new = sum(prices[h:k])

    max_diff = max(0, new - old)

    for r in range(k, n):
        l = r - k + 1
        old += sp[r] - sp[l - 1]
        new += prices[r]
        new -= prices[l - 1 + h]
        max_diff = max(max_diff, new - old)

    return base_sum + max_diff