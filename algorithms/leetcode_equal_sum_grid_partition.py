from typing import List


def can_partition_grid(grid: List[List[int]]) -> bool:
    total_sum = sum(sum(row) for row in grid)

    if total_sum % 2 != 0:
        return False

    target = total_sum // 2

    current_row_sum = 0
    for row in grid:
        current_row_sum += sum(row)
        if current_row_sum == target:
            return True
        if current_row_sum > target:
            break

    current_col_sum = 0
    for col_tuple in zip(*grid):
        current_col_sum += sum(col_tuple)
        if current_col_sum == target:
            return True
        if current_col_sum > target:
            break

    return False


print(can_partition_grid([[1, 1, 1], [2, 1, 1], [3, 1, 2], [4, 1, 2]]))
print(can_partition_grid([[1, 4], [2, 3]]))
print(can_partition_grid([[1, 3], [2, 4]]))
