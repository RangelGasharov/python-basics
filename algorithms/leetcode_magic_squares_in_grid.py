def num_magic_squares_inside(grid: list[list[int]]) -> int:
    magic_set = {(8, 1, 6, 3, 5, 7, 4, 9, 2), (6, 1, 8, 7, 5, 3, 2, 9, 4),
                 (4, 9, 2, 3, 5, 7, 8, 1, 6), (2, 9, 4, 7, 5, 3, 6, 1, 8),
                 (8, 3, 4, 1, 5, 9, 6, 7, 2), (4, 3, 8, 9, 5, 1, 2, 7, 6),
                 (6, 7, 2, 1, 5, 9, 8, 3, 4), (2, 7, 6, 9, 5, 1, 4, 3, 8)}

    n = len(grid)
    m = len(grid[0])
    amount_of_magic_squares = 0

    for i in range(0, n - 2):
        for j in range(0, m - 2):
            current_matrix = (
                grid[i][j], grid[i][j + 1], grid[i][j + 2],
                grid[i + 1][j], grid[i + 1][j + 1], grid[i + 1][j + 2],
                grid[i + 2][j], grid[i + 2][j + 1], grid[i + 2][j + 2]
            )

            if current_matrix in magic_set:
                amount_of_magic_squares += 1

    return amount_of_magic_squares


print(num_magic_squares_inside([[4, 3, 8, 4], [9, 5, 1, 9], [2, 7, 6, 2]]))
print(num_magic_squares_inside([[8]]))
print(num_magic_squares_inside(
    [[9, 9, 5, 1, 9, 5, 5, 7, 2, 5], [9, 1, 8, 3, 4, 6, 7, 2, 8, 9], [4, 1, 1, 5, 9, 1, 5, 9, 6, 4],
     [5, 5, 6, 7, 2, 8, 3, 4, 0, 6], [1, 9, 1, 8, 3, 1, 4, 2, 9, 4], [2, 8, 6, 4, 2, 7, 3, 2, 7, 6],
     [9, 2, 5, 0, 7, 8, 2, 9, 5, 1], [2, 1, 4, 4, 7, 6, 2, 4, 3, 8], [1, 2, 5, 3, 0, 5, 10, 8, 5, 2],
     [6, 9, 6, 8, 8, 4, 3, 6, 0, 9]]))
