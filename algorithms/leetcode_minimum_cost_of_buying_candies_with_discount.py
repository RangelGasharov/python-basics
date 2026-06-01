from typing import List


def minimum_cost(cost: List[int]) -> int:
    cost.sort()
    total_cost = sum(cost)

    for i in range(len(cost) % 3, len(cost), 3):
        total_cost -= cost[i]

    return total_cost


print(minimum_cost([1, 2, 3]))
print(minimum_cost([6, 5, 7, 9, 2, 2]))
print(minimum_cost([5, 5]))
