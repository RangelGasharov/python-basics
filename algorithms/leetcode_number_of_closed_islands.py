from numpy import product


def closed_island(grid: list[list[int]]) -> int:
    m, n = len(grid), len(grid[0])

    def closed(i, j):
        if not (0 <= i < m and 0 <= j < n):
            return False

        if grid[i][j]:
            return True

        grid[i][j] = 1
        return closed(i + 1, j) & closed(i - 1, j) & closed(i, j + 1) & closed(i, j - 1)

    return sum(closed(i, j) for i, j in product(range(m), range(n)) if not grid[i][j])


print(closed_island(
    [[1, 1, 1, 1, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 0, 1],
     [1, 1, 1, 1, 1, 1, 1, 0]]
))
print(closed_island([[0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0]]))
print(closed_island(
    [[1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0, 1], [1, 0, 1, 1, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 1, 1, 0, 1],
     [1, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1]]))
