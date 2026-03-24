from typing import List


def construct_product_matrix(grid: List[List[int]]) -> List[List[int]]:
    rows = len(grid)
    cols = len(grid[0])
    n = rows * cols
    mod = 12345

    flatten_grid = [val for row in grid for val in row]
    res = [1] * n

    current_prefix = 1

    for i in range(n):
        res[i] = current_prefix
        current_prefix = (current_prefix * (flatten_grid[i] % mod)) % mod

    current_suffix = 1
    for i in range(n - 1, -1, -1):
        res[i] = (res[i] * current_suffix) % mod
        current_suffix = (current_suffix * (flatten_grid[i] % mod)) % mod

    return [res[i * cols: (i + 1) * cols] for i in range(rows)]


print(construct_product_matrix([[1, 2], [3, 4]]))
print(construct_product_matrix([[12345], [2], [1]]))
print(construct_product_matrix([[137048688, 395034800, 51674655, 853813001, 66020662, 108245761]]))
print(construct_product_matrix([[1, 10]]))
