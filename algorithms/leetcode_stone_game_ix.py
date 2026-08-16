from typing import List


def stone_game_ix(stones: List[int]) -> bool:
    counts = [0, 0, 0]
    for stone in stones:
        counts[stone % 3] += 1

    if counts[0] % 2 == 0:
        return counts[1] > 0 and counts[2] > 0

    return abs(counts[1] - counts[2]) > 2


print(stone_game_ix([2, 1]))
print(stone_game_ix([2]))
print(stone_game_ix([5, 1, 2, 4, 3]))
