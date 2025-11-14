def range_add_queries(n: int, queries: list[list[int]]) -> list[list[int]]:
    matrix = [[0 for i in range(n)] for x in range(n)]
    diff = [[0] * n for _ in range(n)]

    for query in queries:
        r1, c1, r2, c2 = query
        diff[r1][c1] += 1
        if c2 + 1 < n:
            diff[r1][c2 + 1] -= 1
        if r2 + 1 < n:
            diff[r2 + 1][c1] -= 1
        if r2 + 1 < n and c2 + 1 < n:
            diff[r2 + 1][c2 + 1] += 1
    for i in range(n):
        for j in range(1, n):
            diff[i][j] += diff[i][j - 1]
    for j in range(n):
        for i in range(1, n):
            diff[i][j] += diff[i - 1][j]
    for i in range(n):
        for j in range(n):
            matrix[i][j] += diff[i][j]
    return matrix


print(range_add_queries(3, [[1, 1, 2, 2], [0, 0, 1, 1]]))
print(range_add_queries(2, [[0, 0, 1, 1]]))
