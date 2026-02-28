def concatenated_binary(n: int) -> int:
    mod = 10 ** 9 + 7
    res = 0

    for l in range(1, n.bit_length() + 1):
        start = 1 << (l - 1)
        end = min(n, (1 << l) - 1)
        k = end - start + 1

        r = 1 << l

        if r - 1 == 0:
            inv_r_minus_1 = 1
        else:
            inv_r_minus_1 = pow(r - 1, mod - 2, mod)

        rk = pow(r, k, mod)

        term1 = (start * (rk - 1) % mod) * inv_r_minus_1 % mod
        term2 = ((rk - 1 - k * (r - 1)) % mod) * pow(inv_r_minus_1, 2, mod) % mod

        block_sum = (term1 + term2) % mod
        res = (res * rk + block_sum) % mod

    return res


print(concatenated_binary(3))
print(concatenated_binary(1))
print(concatenated_binary(10000))
print(concatenated_binary(1000000))
