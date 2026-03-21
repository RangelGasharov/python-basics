from typing import List


def reverse_submatrix(grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
    for row in range(k // 2):
        for col in range(k):
            grid[x + row][y + col], grid[x + k - 1 - row][y + col] = grid[x + k - 1 - row][y + col], grid[x + row][y + col]
    return grid


print(reverse_submatrix([[3, 4, 2, 3], [2, 3, 4, 2]], 0, 2, 2))
print(reverse_submatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 0, 0, 3))
