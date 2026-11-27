from typing import List


def maximum_sale_items(items: List[List[int]], budget: int) -> int:
    factors, prices = zip(*items)
    have = [0] * (max(factors) + 1)

    for factor in factors:
        have[factor] += 1
    gains = {factor: sum(have[factor::factor]) for factor in set(factors)}

    cheapest = min(prices)
    best = [money // cheapest for money in range(budget + 1)]

    for factor, price in items:
        if (gain := gains[factor]) > price // cheapest:
            for money in range(budget, price - 1, -1):
                best[money] = max(best[money], best[money - price] + gain)
    return best[budget]


print(maximum_sale_items([[6, 2], [2, 6], [3, 4]], 9))
print(maximum_sale_items([[2, 4], [3, 2], [4, 1], [6, 4], [12, 4]], 8))
