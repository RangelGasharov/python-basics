def largestMagicSquare(grid):
    r, c = len(grid), len(grid[0])

    row = [[0] * (c + 1) for _ in range(r)]
    col = [[0] * c for _ in range(r + 1)]

    for i in range(r):
        for j in range(c):
            row[i][j + 1] = row[i][j] + grid[i][j]

    for j in range(c):
        for i in range(r):
            col[i + 1][j] = col[i][j] + grid[i][j]

    ans = 1

    for i in range(r):
        for j in range(c):
            for size in range(min(r - i, c - j), ans, -1):
                if is_magic(grid, row, col, i, j, size):
                    ans = size
                    break
    return ans


def is_magic(self, g, r, c, x, y, l):
    target = r[x][y + l] - r[x][y]

    for i in range(l):
        if r[x + i][y + l] - r[x + i][y] != target:
            return False

    for j in range(l):
        if c[x + l][y + j] - c[x][y + j] != target:
            return False

    d1 = d2 = 0
    for k in range(l):
        d1 += g[x + k][y + k]
        d2 += g[x + l - 1 - k][y + k]

    return d1 == target and d2 == target


print(largestMagicSquare([[7, 1, 4, 5, 6], [2, 5, 1, 6, 4], [1, 5, 4, 3, 2], [1, 2, 7, 3, 4]]))
print(largestMagicSquare([[5, 1, 3, 1], [9, 3, 3, 1], [1, 3, 3, 8]]))
