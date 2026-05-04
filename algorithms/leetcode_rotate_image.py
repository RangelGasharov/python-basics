from typing import List


def rotate(matrix: List[List[int]]) -> None:
    rows = len(matrix)
    cols = len(matrix[0])

    for row in range(rows):
        for col in range(row + 1, cols):
            matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
    for row in range(rows):
        for col in range(cols // 2):
            matrix[row][col], matrix[row][cols - col - 1] = matrix[row][cols - col - 1], matrix[row][col]


test_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotate(test_matrix)
print(test_matrix)

test_matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
rotate(test_matrix)
print(test_matrix)
