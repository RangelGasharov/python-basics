from typing import List


def rotateTheBox(box_grid: List[List[str]]) -> List[List[str]]:
    rows = len(box_grid)
    cols = len(box_grid[0])

    for row in range(rows):
        p = 0
        for col in range(cols):
            if box_grid[row][col] == ".":
                box_grid[row][col], box_grid[row][p] = box_grid[row][p], box_grid[row][col]
                p += 1
            elif box_grid[row][col] == "*":
                p = col + 1

    result = [[""] * rows for _ in range(cols)]
    for row in range(rows):
        for col in range(cols):
            result[col][rows - 1 - row] = box_grid[row][col]

    return result


print(rotateTheBox([["#", ".", "#"]]))
print(rotateTheBox([["#", ".", "*", "."], ["#", "#", "*", "."]]))
print(rotateTheBox([["#", "#", "*", ".", "*", "."], ["#", "#", "#", "*", ".", "."], ["#", "#", "#", ".", "#", "."]]))
