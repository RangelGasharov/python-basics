def count_unguarded(m: int, n: int, guards: list[list[int]], walls: list[list[int]]) -> int:
    cells = [[0 for col in range(n)] for row in range(m)]
    for wall in walls:
        cells[wall[0]][wall[1]] = 2
    for guard in guards:
        cells[guard[0]][guard[1]] = 2

    for guard in guards:
        row = guard[0]
        col = guard[1]
        for i in range(col - 1, -1, -1):
            if cells[row][i] == 2:
                break
            cells[row][i] = 1
        for i in range(col + 1, n):
            if cells[row][i] == 2:
                break
            cells[row][i] = 1
        for i in range(row - 1, -1, -1):
            if cells[i][col] == 2:
                break
            cells[i][col] = 1
        for i in range(row + 1, m):
            if cells[i][col] == 2:
                break
            cells[i][col] = 1

    unguarded_cells = 0

    for i in range(m):
        for j in range(n):
            unguarded_cells += cells[i][j] == 0
    return unguarded_cells


print(count_unguarded(4, 6, [[0, 0], [1, 1], [2, 3]], [[0, 1], [2, 2], [1, 4]]))
print(count_unguarded(3, 3, [[1, 1]], [[0, 1], [1, 0], [2, 1], [1, 2]]))
