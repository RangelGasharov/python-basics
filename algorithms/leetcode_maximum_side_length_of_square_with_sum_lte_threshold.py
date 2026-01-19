def max_side_length(mat: list[list[int]], threshold: int) -> int:
    m = len(mat)
    n = len(mat[0])

    pre = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m):
        row_sum = 0
        for j in range(n):
            row_sum += mat[i][j]
            pre[i + 1][j + 1] = pre[i][j + 1] + row_sum

    def square_exists(k: int) -> bool:
        for i in range(k, m + 1):
            for j in range(k, n + 1):
                s = (pre[i][j] - pre[i - k][j] - pre[i][j - k] + pre[i - k][j - k])
                if s <= threshold:
                    return True
        return False

    result = 0

    for k in range(1, min(m, n) + 1):
        if square_exists(k):
            result = k
        else:
            break
    return result


print(max_side_length([[1, 1, 3, 2, 4, 3, 2], [1, 1, 3, 2, 4, 3, 2], [1, 1, 3, 2, 4, 3, 2]], 4))
print(max_side_length([[2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2]], 1))
