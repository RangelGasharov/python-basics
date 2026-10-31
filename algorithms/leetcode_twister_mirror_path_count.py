from typing import List


def unique_paths(grid: List[List[int]]) -> int:
    mod = 10 ** 9 + 7
    down = [1] + [0] * (len(grid[0]) - 1)

    for row in grid:
        right = 0
        for j, mirror in enumerate(row):
            if mirror:
                right, down[j] = down[j], right
            else:
                right = down[j] = (right + down[j]) % mod
    return down[-1]


print(unique_paths([[0, 1, 0], [0, 0, 1], [1, 0, 0]]))
print(unique_paths([[0, 0], [0, 0]]))
print(unique_paths([[0, 1, 1], [1, 1, 0]]))
