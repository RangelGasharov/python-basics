def reverse_bits(n: int) -> int:
    res = 0
    for i in range(32):
        res = (res << 1) | (n & 1)
        n >>= 1
    return res


print(reverse_bits(43261596))
print(reverse_bits(2147483644))
