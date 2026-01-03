def num_of_ways(n: int) -> int:
    mod = 10 ** 9 + 7
    a = b = 6

    for _ in range(2, n + 1):
        a, b = (2 * a + 2 * b) % mod, (2 * a + 3 * b) % mod

    return (a + b) % mod


print(num_of_ways(1))
print(num_of_ways(2))
print(num_of_ways(3))
print(num_of_ways(5000))
