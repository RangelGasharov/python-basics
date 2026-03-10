def number_of_stable_arrays(zero: int, one: int, limit: int) -> int:
    mod = 1000000007
    max_n = zero + one

    fact = [0] * (max_n + 1)
    inv_fact = [0] * (max_n + 1)

    fact[0] = 1
    inv_fact[0] = 1
    for i in range(1, max_n + 1):
        fact[i] = (fact[i - 1] * i) % mod

    inv_fact[max_n] = pow(fact[max_n], mod - 2, mod)
    for i in range(max_n - 1, 0, -1):
        inv_fact[i] = (inv_fact[i + 1] * (i + 1)) % mod

    def C(n, k):
        if k < 0 or k > n:
            return 0
        return fact[n] * inv_fact[k] % mod * inv_fact[n - k] % mod

    def F(n, k, l):
        if k <= 0 or k > n:
            return 0
        res = 0
        max_j = (n - k) // l
        for j in range(max_j + 1):
            term = C(k, j) * C(n - j * l - 1, k - 1) % mod
            if j & 1:
                res = (res - term + mod) % mod
            else:
                res = (res + term) % mod
        return res

    max_k = min(zero, one + 1)
    f_one = [0] * (max_k + 2)
    for k in range(1, max_k + 2):
        f_one[k] = F(one, k, limit)

    ans = 0
    for k in range(1, max_k + 1):
        fz = F(zero, k, limit)
        if fz == 0:
            continue
        fo = (f_one[k - 1] + 2 * f_one[k] + f_one[k + 1]) % mod
        ans = (ans + fz * fo) % mod

    return ans


print(number_of_stable_arrays(1, 1, 2))
print(number_of_stable_arrays(1, 2, 1))
print(number_of_stable_arrays(2, 2, 2))
print(number_of_stable_arrays(3, 3, 2))
print(number_of_stable_arrays(200, 200, 50))
print(number_of_stable_arrays(1000, 800, 150))
print(number_of_stable_arrays(1000, 1000, 10))
