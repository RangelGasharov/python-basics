def find_complement(n):
    if n == 0:
        return 1

    bit_length = n.bit_length()

    mask = (1 << bit_length) - 1

    return n ^ mask


print(find_complement(0))
print(find_complement(1))
print(find_complement(2))
print(find_complement(5))
print(find_complement(7))
print(find_complement(10))
print(find_complement(1234567))
