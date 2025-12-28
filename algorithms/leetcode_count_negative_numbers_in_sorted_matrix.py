def count_negatives(grid: list[list[int]]) -> int:
    num_of_negative_nums = 0
    for matrix in grid:
        n = len(matrix)
        left = 0
        right = n - 1
        first_negative_index = n

        while left <= right:
            middle = (left + right) // 2
            if matrix[middle] < 0:
                first_negative_index = middle
                right = middle - 1
            else:
                left = middle + 1

        num_of_negative_nums += n - first_negative_index
    return num_of_negative_nums


print(count_negatives([[4, 3, 2, -1, -1, -1, -2, -3]]))
print(count_negatives([[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]))
print(count_negatives([[-1, -1, -2, -3]]))
