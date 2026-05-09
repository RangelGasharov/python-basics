from typing import List


def rotate_grid(grid: List[List[int]], k: int) -> List[List[int]]:
    rows = len(grid)
    cols = len(grid[0])

    total_layers = min(rows, cols) // 2

    for layer in range(total_layers):
        elements = []

        top = left = layer
        bottom = rows - layer - 1
        right = cols - layer - 1

        for col in range(left, right + 1):
            elements.append(grid[top][col])

        for row in range(top + 1, bottom):
            elements.append(grid[row][right])

        for col in range(right, left - 1, -1):
            elements.append(grid[bottom][col])

        for row in range(bottom - 1, top, -1):
            elements.append(grid[row][left])

        size = len(elements)
        index = k % size

        for col in range(left, right + 1):
            grid[top][col] = elements[index]
            index = (index + 1) % size

        for row in range(top + 1, bottom):
            grid[row][right] = elements[index]
            index = (index + 1) % size

        for col in range(right, left - 1, -1):
            grid[bottom][col] = elements[index]
            index = (index + 1) % size

        for row in range(bottom - 1, top, -1):
            grid[row][left] = elements[index]
            index = (index + 1) % size

    return grid


print(rotate_grid([[40, 10], [30, 20]], 1))
print(rotate_grid([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], 2))
