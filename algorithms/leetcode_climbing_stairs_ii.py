from cmath import inf


def climb_stairs(n: int, costs: list[int]) -> int:
    costs = [0] + costs
    a, b, c = costs[n], inf, inf
    for i in reversed(range(n)):
        a, b, c = costs[i] + min(a + 1, b + 4, c + 9), a, b
    return a


print(climb_stairs(4, [1, 2, 3, 4]))
print(climb_stairs(4, [5, 1, 6, 2]))
print(climb_stairs(3, [9, 8, 3]))
