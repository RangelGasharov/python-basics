def zig_zag_arrays(n: int, l: int, r: int) -> int:
    mod = 1_000_000_007
    m = r - l + 1
    dp = [1] * m

    for i in range(2, n + 1):
        dp.reverse()
        s = 0
        for j in range(m):
            dp[j], s = s, (s + dp[j]) % mod

    return (sum(dp) % mod << 1) % mod


print(zig_zag_arrays(3, 4, 5))
print(zig_zag_arrays(3, 1, 3))
