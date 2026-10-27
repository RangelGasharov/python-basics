def create_grid(m: int, n: int) -> list[str]:
    grid = ["#" * (n - 1) + "."] * m
    grid[0] = "." * n
    return grid


print(create_grid(1, 4))
print(create_grid(2, 3))
print(create_grid(3, 3))
