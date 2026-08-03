from linecache import cache
from typing import List


def stone_game_iii(self, stone_value: List[int]) -> str:
    n = len(stone_value)

    @cache
    def max_diff(i:int) -> int:
        if i == n:
            return 0
        a = b = c = -5e7

        if i < n:
            a = stone_value[i] - max_diff(i + 1)
        if i + 1 < n:
            b = stone_value[i] + stone_value[i + 1] - max_diff(i + 2)
        if i + 2 < n:
            c = stone_value[i] + stone_value[i + 1] + stone_value[i + 2] - max_diff(i + 3)

        return max(a, b, c)

    d = max_diff(0)
    return  "Alice" if d > 0 else "Bob" if d < 0 else "Tie"