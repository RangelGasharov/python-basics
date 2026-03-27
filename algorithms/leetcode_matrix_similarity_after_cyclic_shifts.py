from typing import List


def are_similar(mat: List[List[int]], k: int) -> bool:
    rows = len(mat)
    cols = len(mat[0])

    k %= cols

    for r in range(rows):
        for c in range(cols):
            if not mat[r][c] == mat[r][(c + k) % cols]:
                return False
    return True


print(are_similar([[9, 1, 8, 9, 2, 9, 1, 8, 9, 2], [10, 2, 7, 8, 9, 10, 2, 7, 8, 9],
                   [7, 6, 6, 9, 5, 7, 6, 6, 9, 5]], 3))
print(are_similar([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 4))
print(are_similar([[1, 2, 1, 2], [5, 5, 5, 5], [6, 3, 6, 3]], 2))
print(are_similar([[2, 2], [2, 2]], 3))
