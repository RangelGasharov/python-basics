def minimum_cost(cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
    total = 0
    if need1 <= need2:
        if costBoth < cost1 + cost2:
            total += costBoth * need1
            need2 -= need1
        else:
            total += cost1 * need1
        need1 = 0
    else:
        if costBoth < cost1 + cost2:
            total += costBoth * need2
            need1 -= need2
        else:
            total += cost2 * need2
        need2 = 0

    total += need1 * min(cost1, costBoth) + need2 * min(cost2, costBoth)
    return total


print(minimum_cost(3, 2, 1, 3, 2))
print(minimum_cost(5, 4, 15, 2, 3))
print(minimum_cost(5, 4, 15, 0, 0))
