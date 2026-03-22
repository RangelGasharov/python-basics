from typing import List


def find_rotation(mat: List[List[int]], target: List[List[int]]) -> bool:
    for i in range(4):
        if mat == target:
            return True
        target = [list(row[::-1]) for row in zip(*target)]
    return False


print(find_rotation([[0, 1], [1, 0]], [[1, 0], [0, 1]]))
print(find_rotation([[0, 1], [1, 1]], [[1, 0], [0, 1]]))
print(find_rotation([[0, 0, 0], [0, 1, 0], [1, 1, 1]], [[1, 1, 1], [0, 1, 0], [0, 0, 0]]))
