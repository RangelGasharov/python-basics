from typing import List


def shift_grid(grid: List[List[int]], k: int) -> List[List[int]]:
    if not k:
        return grid

    rows, cols = len(grid), len(grid[0])
    n = rows * cols
    k %= n

    if not k:
        return grid

    def shift(i, j):
        while i < j:
            grid[i // cols][i % cols], grid[j // cols][j % cols] = grid[j // cols][j % cols], grid[i // cols][i % cols]
            i += 1
            j -= 1

    shift(0, n - 1)
    shift(0, k - 1)
    shift(k, n - 1)

    return grid


print(shift_grid([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1))
print(shift_grid([[3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10], [12, 0, 21, 13]], 4))
print(shift_grid([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 9))
