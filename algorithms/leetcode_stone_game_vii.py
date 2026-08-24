from typing import List


def stone_game_viii(stones: List[int]) -> int:
    total = sum(stones)
    best = total
    p = total
    for i in range(len(stones) - 1, 1, -1):
        p -= stones[i]
        best = max(best, p - best)
    return best


print(stone_game_viii([-1, 2, -3, 4, -5]))
print(stone_game_viii([7, -6, 5, 10, 5, -2, -6]))
print(stone_game_viii([-10, -12]))
