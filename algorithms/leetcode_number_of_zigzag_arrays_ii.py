def zig_zag_arrays(n: int, l: int, r: int) -> int:
    mod = 1000000007

    m = r - l + 1
    size = 2 * m

    def multiply(A, B):
        C = [[0] * size for _ in range(size)]

        for i in range(size):
            for k in range(size):
                if A[i][k] == 0:
                    continue

                cur = A[i][k]

                for j in range(size):
                    if B[k][j] == 0:
                        continue

                    C[i][j] = (C[i][j] + cur * B[k][j]) % mod
        return C

    T = [[0] * size for _ in range(size)]

    for x in range(m):
        for y in range(x + 1, m):
            T[x][m + y] = 1

        for y in range(x):
            T[m + x][y] = 1

    result = [[0] * size for _ in range(size)]
    for i in range(size):
        result[i][i] = 1

    power = n - 1

    while power:
        if power & 1:
            result = multiply(result, T)

        T = multiply(T, T)
        power >>= 1

    answer = 0

    for i in range(size):
        row_sum = sum(result[i]) % mod
        answer = (answer + row_sum) % mod

    return answer


print(zig_zag_arrays(3, 4, 5))
print(zig_zag_arrays(3, 1, 3))
