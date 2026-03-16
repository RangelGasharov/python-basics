from typing import List


def get_biggest_three(grid: List[List[int]]) -> List[int]:
    cols = len(grid[0])
    rows = len(grid)

    max_len = (min(cols, rows) - 1) // 2
    results = set()

    for r in range(rows):
        for c in range(cols):
            results.add(grid[r][c])

    for k in range(1, max_len + 1):
        for r in range(k, rows - k):
            for c in range(k, cols - k):
                current_sum = 0
                for i in range(k):
                    current_sum += grid[r - k + i][c + i]
                    current_sum += grid[r + i][c + k - i]
                    current_sum += grid[r + k - i][c - i]
                    current_sum += grid[r - i][c - k + i]
                results.add(current_sum)
    return sorted(list(results), reverse=True)[:3]


print(get_biggest_three([[3, 4, 5, 1, 3], [3, 3, 4, 2, 3], [20, 30, 200, 40, 10], [1, 5, 5, 4, 1], [4, 3, 2, 2, 5]]))
print(get_biggest_three([[1, 2, 3], [4, 5, 6], [7, 8, 9], [7, 8, 9]]))
print(get_biggest_three([[1, 1, 1, 1], [1, 2, 3, 1], [1, 1, 1, 1]]))
