from typing import List


def largestSubmatrix(matrix: List[List[int]]) -> int:
    result = 0
    cols = len(matrix[0])
    rows = len(matrix)

    col_heights = [0] * cols

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 0:
                col_heights[c] = 0
            col_heights[c] += matrix[r][c]

        sorted_heights = sorted(col_heights, reverse=True)

        for i in range(cols):
            result = max(result, sorted_heights[i] * (i + 1))

    return result


print(largestSubmatrix([[0, 0, 1], [1, 1, 1], [1, 0, 1]]))
print(largestSubmatrix([[1, 1, 0], [1, 0, 1]]))
print(largestSubmatrix(
    [[1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1],
     [1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1],
     [1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0]]))
