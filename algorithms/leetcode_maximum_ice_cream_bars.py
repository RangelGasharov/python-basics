from typing import List


def max_ice_cream(costs: List[int], coins: int) -> int:
    costs.sort()
    max_cost = 0
    for cost in costs:
        if cost > coins:
            return max_cost
        max_cost += 1
        coins -= cost
    return max_cost


print(max_ice_cream([1, 3, 2, 4, 1], 7))
print(max_ice_cream([10, 6, 8, 7, 7, 8], 5))
print(max_ice_cream([1, 6, 3, 1, 2, 5], 20))
