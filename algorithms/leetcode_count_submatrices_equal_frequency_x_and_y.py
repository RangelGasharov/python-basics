from typing import List


def number_of_submatrices(grid: List[List[str]]) -> int:
    rows = len(grid)
    cols = len(grid[0])
    sum_x = [0] * cols
    sum_y = [0] * cols
    result = 0

    for i in range(rows):
        x_count = 0
        y_count = 0

        for j in range(cols):
            if grid[i][j] == "X":
                x_count += 1
            elif grid[i][j] == "Y":
                y_count += 1

            sum_x[j] += x_count
            sum_y[j] += y_count

            if sum_x[j] > 0 and sum_x[j] == sum_y[j]:
                result += 1

    return result


print(number_of_submatrices([["X", "Y", "."], ["Y", ".", "."]]))
print(number_of_submatrices([["X", "X"], ["X", "Y"]]))
print(number_of_submatrices([[".", "."], [".", "."]]))
