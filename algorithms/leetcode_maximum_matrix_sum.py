def max_matrix_sum(matrix: list[list[int]]) -> int:
    num_of_negative = 0
    n = len(matrix)
    m = len(matrix[0])
    sum_numbers = 0
    smallest_absolute = abs(matrix[0][0])

    for i in range(n):
        for j in range(m):
            current_num = matrix[i][j]
            if current_num < 0:
                num_of_negative += 1
            if abs(current_num) < smallest_absolute:
                smallest_absolute = abs(current_num)
            sum_numbers += abs(current_num)
    if num_of_negative % 2 == 0:
        return sum_numbers
    return sum_numbers - 2 * smallest_absolute

print(max_matrix_sum([[1,2,3],[-1,-2,-3],[1,2,3]]))