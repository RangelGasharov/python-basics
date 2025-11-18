def is_one_bit_character(bits: list[int]) -> bool:
    n = len(bits)
    i = 0
    while i < n - 1:
        i += 1 + bits[i]
    return i == n - 1


print(is_one_bit_character([1, 0, 0]))
print(is_one_bit_character([1, 1, 1, 0]))
print(is_one_bit_character([0]))
print(is_one_bit_character([1, 0]))
