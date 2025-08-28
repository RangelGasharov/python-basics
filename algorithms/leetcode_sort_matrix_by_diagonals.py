def sort_matrix_diagonals(matrix):
    if len(matrix) == 0:
        return []

    side = len(matrix)
    result = [[None for _ in range(side)] for _ in range(side)]

    for offset in range(-(side - 1), side):
        diagonal = []

        for i in range(side):
            j = i - offset
            if 0 <= j < side:
                diagonal.append(matrix[i][j])

        if offset >= 0:
            diagonal.sort(reverse=True)
        else:
            diagonal.sort()

        k = 0
        for i in range(side):
            j = i - offset
            if 0 <= j < side:
                result[i][j] = diagonal[k]
                k += 1

    return result


print(sort_matrix_diagonals([
    [1, 7, 3],
    [9, 8, 2],
    [4, 5, 6]
]))

print(sort_matrix_diagonals([
    [0, 1],
    [1, 2]
]))
