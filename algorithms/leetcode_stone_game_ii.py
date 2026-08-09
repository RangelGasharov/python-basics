from functools import cache
from typing import List


def stone_game_ii(piles: List[int]) -> int:
    for i in range(len(piles) - 2, -1, -1):
        piles[i] += piles[i + 1]

    @cache
    def dfs(i, M):
        if i + M * 2 >= len(piles):
            return piles[i]

        return piles[i] - min(dfs(i + j, max(M, j)) for j in range(1, M * 2 + 1))

    return dfs(0, 1)


print(stone_game_ii([2, 7, 9, 4, 4]))
print(stone_game_ii([1, 2, 3, 4, 5, 100]))
print(stone_game_ii([1, 2, 35, 100]))