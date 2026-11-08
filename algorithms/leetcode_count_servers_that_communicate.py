def count_servers(grid: list[list[int]]) -> int:
    col = [sum(c) for c in zip(*grid)]
    total = 0
    for r in grid:
        s = sum(r)
        if s > 1:
            total += s
        elif s == 1 and col[r.index(1)] > 1:
            total += 1
    return total


print(count_servers([[1, 0], [0, 1]]))
print(count_servers([[1, 0], [1, 1]]))
print(count_servers([[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]]))
